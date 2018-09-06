
#chapter 2 question 2.6 is palindrome --> accidentally solved for anagram

def ll_is_anagram(ll):
    if ll:
        data = {}
        cur = ll.head
        while cur:
            if data[cur.data] == 0:
                data[cur.data] +=1
            elif data[cur.data] == 1:
                data[cur.data] -= 1
            else:
                data[cur.data] = 1
            cur = cur.next
        if sum(data.values()) > 1:
            return False
        else:
            return True
    else:
        return False


    # next solution for PALINDROME: 

    # build a string or list with ll data
    # split in half (make sure to account for even or odd)
    # compare the two halves --> if first half equals reverse of second half
    # return true, else return false

    # alternatively: use a stack to create list with ordered data of nodes,
    # then walk linked list to compare!