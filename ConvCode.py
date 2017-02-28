cs_traceback(r_codeword, trellis, decoding_type,
                   path_metrics, paths, decoded_symbols,
                   decoded_bits, tb_count, t, count,
                   tb_depth, current_number_states):
 
    #cdef int state_num, i, j, number_previous_states, previous_state, \
    #        previous_input, i_codeword, number_found, min_idx, \
    #        current_state, dec_symbol
 
    k = trellis.k
    n = trellis.n
    number_states = trellis.number_states
    number_inputs = trellis.number_inputs
 
    branch_metric = 0.0
 
    next_state_table = trellis.next_state_table
    output_table = trellis.output_table
    pmetrics = np.empty(number_inputs)
    i_codeword_array = np.empty(n, 'int')
    index_array = np.empty([number_states, 2], 'int')
    decoded_bitarray = np.empty(k, 'int')
 
    # Loop over all the current states (Time instant: t)
    for state_num in range(current_number_states):
 
        # Using the next state table find the previous states and inputs
        # leading into the current state (Trellis)
        number_found = _where_c(next_state_table, number_states, number_inputs, state_num, index_array)
 
        # Loop over all the previous states (Time instant: t-1)
        for i in range(number_found):
 
            previous_state = index_array[i, 0]
            previous_input = index_array[i, 1]
 
            # Using the output table, find the ideal codeword
            i_codeword = output_table[previous_state, previous_input]
            #dec2bitarray_c(i_codeword, n, i_codeword_array)
            i_codeword_array = dec2bitarray(i_codeword, n)
 
            # Compute Branch Metrics
            if decoding_type == 'hard':
                #branch_metric = hamming_dist_c(r_codeword.astype(int), i_codeword_array.astype(int), n)
                branch_metric = hamming_dist(r_codeword.astype(int), i_codeword_array.astype(int))
            elif decoding_type == 'soft':
                pass
            elif decoding_type == 'unquantized':
                i_codeword_array = 2*i_codeword_array - 1
                branch_metric = euclid_dist(r_codeword, i_codeword_array)
            else:
                pass
 
            # ADD operation: Add the branch metric to the
            # accumulated path metric and store it in the temporary array
            pmetrics[i] = path_metrics[previous_state, 0] + branch_metric
 
        # COMPARE and SELECT operations
        # Compare and Select the minimum accumulated path metric
        path_metrics[state_num, 1] = pmetrics.min()
 
        # Store the previous state corresponding to the minimum
        # accumulated path metric
        min_idx = pmetrics.argmin()
        paths[state_num, tb_count] = index_array[min_idx, 0]
 
        # Store the previous input corresponding to the minimum
        # accumulated path metric
        decoded_symbols[state_num, tb_count] = index_array[min_idx, 1]
 
    if t >= tb_depth - 1:
        current_state = path_metrics[:,1].argmin()
 
        # Traceback Loop
        for j in reversed(range(1, tb_depth)):
 
            dec_symbol = decoded_symbols[current_state, j]
            previous_state = paths[current_state, j]
            decoded_bitarray = dec2bitarray(dec_symbol, k)
            decoded_bits[(t-tb_depth-1)+(j+1)*k+count:(t-tb_depth-1)+(j+2)*k+count] =  \
                    decoded_bitarray
            current_state = previous_state
 
        paths[:,0:tb_depth-1] = paths[:,1:]
        decoded_symbols[:,0:tb_depth-1] = decoded_symbols[:,1:]
