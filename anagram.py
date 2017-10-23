def question1(s, t):
        string_length = len(s)
        sub_length = len(t)

        for x in range(0,(string_length-sub_length)):
                new_string = s[x:x+sub_length]
                if anagram_test(new_string,t):
                        return True

def anagram_test(s1, s2):
        if (sorted(s1) == sorted(s2)):
                return True


def main():
        s = "udacity"
        t = "cd"

        if question1(s,t):
                print ("Test Pass")
        else:
                print ("Test Failed")


if __name__ == '__main__':
        main()
