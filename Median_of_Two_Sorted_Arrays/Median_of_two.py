class Train(object):
    """
    train myself
    """
    def find_median(self, a):
        """return median"""
        len_a = len(a)
        i = 0
        ans = 0
        if len_a % 2 == 0:
            i = int(len_a / 2)
            j = int(i - 1)
            ans =  (a[i] + a[j]) / 2
        else:
            i = len_a - 1
            i = int(i/2)
            ans =  a[i]
        return float(ans)


    def find_ans(self, a , b):
        """
        Join two sorted arrays
        """
        len_a = len(a)
        len_b = len(b)
        length = len_a + len_b
        current_a = 0
        current_b = 0
        final = []
        if len_a == 0:
            final = b
        elif len_b == 0:
            final = a
        else:
            for i in range(length):
                val_a =  a[current_a]
                val_b = b[current_b]
                if val_a < val_b:
                    final.append(val_a)
                    current_a += 1
                elif val_a > val_b:
                    final.append(val_b)
                    current_b += 1
                else:
                    final.append(val_a)
                    final.append(val_b)
                    current_a += 1
                    current_b += 1
                if current_a == len_a:
                    final += b[current_b:]
                    break
                if current_b == len_b:
                    final += a[current_a:]
                    break
        print(final)
        return self.find_median(final)

a = []
b = [3,4]
obj = Train()
print(obj.find_ans(a,b))