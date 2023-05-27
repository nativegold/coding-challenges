def solution(s):
    answer = len(s)

    for length in range(len(s) // 2, 0, -1):
        count = 1
        sp_b = ""
        made_str = ""
        split_s = [s[j:j + length] for j in range(0, len(s), length)]

        for sp in split_s:
            if sp_b == sp:
                count += 1
            else:
                if count > 1:
                    made_str += str(count) + sp_b
                else:
                    made_str += sp_b
                sp_b = sp
                count = 1
            last = sp

        if count > 1:
            made_str += str(count) + last
        else:
            made_str += last

        if answer > len(made_str):
            answer = len(made_str)

    return answer
