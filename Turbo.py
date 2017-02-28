ckward_recursion(trellis, msg_length, noise_variance,
                        sys_symbols, non_sys_symbols, branch_probs,
                        priors, b_state_metrics):
 
    n = trellis.n
    number_states = trellis.number_states
    number_inputs = trellis.number_inputs
 
    codeword_array = empty(n, 'int')
    next_state_table = trellis.next_state_table
    output_table = trellis.output_table
 
    # Backward recursion
    for reverse_time_index in reversed(xrange(1, msg_length+1)):
 
        for current_state in xrange(number_states):
            for current_input in xrange(number_inputs):
                next_state = next_state_table[current_state, current_input]
                code_symbol = output_table[current_state, current_input]
                codeword_array = dec2bitarray(code_symbol, n)
                parity_bit = codeword_array[1]
                msg_bit = codeword_array[0]
                rx_symbol_0 = sys_symbols[reverse_time_index-1]
                rx_symbol_1 = non_sys_symbols[reverse_time_index-1]
                branch_prob = _compute_branch_prob(msg_bit, parity_bit,
                                                   rx_symbol_0, rx_symbol_1,
                                                   noise_variance)
                branch_probs[current_input, current_state, reverse_time_index-1] = branch_prob
                b_state_metrics[current_state, reverse_time_index-1] += \
                        (b_state_metrics[next_state, reverse_time_index] * branch_prob *
                                priors[current_input, reverse_time_index-1])
 
        b_state_metrics[:,reverse_time_index-1] /= \
            b_state_metrics[:,reverse_time_index-1].sum()
