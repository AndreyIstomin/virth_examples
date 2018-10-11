

def prepare_kmp(pattern):

    prefix_func = [0] * (len(pattern) - 1)# by default prefix func for one element string is zero

    # loop over each substring except the first one (one element string)
    for last_element_in_substr in range(1, len(pattern) - 1):

        prev_prefix = prefix_func[last_element_in_substr - 1] # get prefix func value for prev substr

        element_after_prev_prefix = prev_prefix

        while prev_prefix > 0 and pattern[element_after_prev_prefix] != pattern[last_element_in_substr]:
            # lets check the same for the prefix of the prefix
            prev_prefix = prefix_func[prev_prefix - 1]
            element_after_prev_prefix = prev_prefix

        if pattern[element_after_prev_prefix] == pattern[last_element_in_substr]:

            new_prefix = prev_prefix + 1
            # found correct prefix func value for the current substr
            prefix_func[last_element_in_substr] = new_prefix

        else:
            # got k = 0 and found out that there is not any prefix for the current substr

            prefix_func[last_element_in_substr] = 0

    for i in range(0, len(pattern) - 1):

        if prefix_func[i] == 0 and pattern[0] == pattern[i + 1]:
            prefix_func[i] = -1

    return prefix_func


def run_kmp(text, pattern, prefix_func):

    text_index = 0
    pattern_index = 0

    while text_index < len(text) and pattern_index < len(pattern):

        while pattern_index > 0 and text[text_index] != pattern[pattern_index]:

            # DEBUG INFO #################################################################
            text_symbol = text[text_index]
            pattern_symbol = pattern[pattern_index]
            not_equal = text[text_index] != pattern[pattern_index]
            print(text)
            print('%s%s' % (' ' * (text_index - pattern_index), pattern))
            if not_equal:
                print('%s^ (%s != %s)' % (' ' * text_index, text_symbol, pattern_symbol))
            ##############################################################################

            # lets check the same for the prefix:
            pattern_index = prefix_func[pattern_index - 1]

        # move on comparing symbol by symbol
        if pattern_index == -1 or text[text_index] == pattern[pattern_index]:
            pattern_index += 1

            # DEBUG INFO #################################################################
        else:
            text_symbol = text[text_index]
            pattern_symbol = pattern[pattern_index]
            not_equal = text[text_index] != pattern[pattern_index]
            print(text)
            print('%s%s' % (' ' * (text_index - pattern_index), pattern))
            if not_equal:
                print('%s^ (%s != %s)' % (' ' * text_index, text_symbol, pattern_symbol))
            ##############################################################################

        if pattern_index == len(pattern):
            break

        text_index += 1

    if pattern_index == len(pattern):

        print ('success: %d' % (text_index - len(pattern)))


if __name__ == "__main__":

    pattern = 'abcabc'
    prefix_func = prepare_kmp(pattern + ' ')

    print(prefix_func)

    run_kmp('abcbadabababcaabcabcabd', pattern, prefix_func)
