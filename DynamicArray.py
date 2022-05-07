import ctypes


class DynamicArray(object):
    # initially length of array is 0, capacity is 1
    def __init__(self):
        self.n = 0
        self.cap = 1
        self.A = self.__make_array(self.cap)

    # method to return number of elements in array or length of array
    def __len__(self):
        return self.n

    # method to get element at particular index
    def __getitem__(self, index):
        if 0 <= index < self.n:
            return self.A[index]
        return IndexError("Index out of range!")

    # method assign the value to particular index
    def __setitem__(self, index, value):
        if 0 <= index < self.n:
            self.A[index] = value
        return IndexError("Index out of range!")

    # private method to resize the array
    def __resize(self, new_cap):
        b = self.__make_array(new_cap)
        for i in range(self.n):
            b[i] = self.A[i]
        self.A = b
        self.cap = new_cap

    # private method of creating the array with given capacity
    def __make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()

    # method to append element to the array
    def append(self, element):
        if self.n == self.cap:
            # if not enough space resize the array to twice the size
            self.__resize(2 * self.cap)
        self.A[self.n] = element
        self.n += 1

    # method to pop element from the array
    def pop(self, index=None):
        poped = self.A[index] if index else self.A[self.n - 1]
        b = self.__make_array(self.cap)
        if index is not None:
            for i in range(self.n - 1):
                if i < index:
                    b[i] = self.A[i]
                else:
                    b[i] = self.A[i + 1]
            self.A = b
        self.n -= 1
        return poped

    # method to insert element at any given index
    def insert(self, index, element):
        if not 0 <= index < self.n:
            return IndexError("Index out of range!")
        if self.n == self.cap:
            # if not enough space resize the array to twice the size
            self.__resize(2 * self.cap)
            self.cap *= 2
        b = self.__make_array(self.cap)
        for i in range(self.n + 1):
            if i < index:
                b[i] = self.A[i]
            elif i == index:
                b[i] = element
            else:
                b[i] = self.A[i - 1]
        self.A = b
        self.n += 1


if __name__ == "__main__":
    Arr = DynamicArray()
    Arr.append(1)
    print(Arr[0])
    print(len(Arr))
    Arr.append(2)
    print(Arr[1])
    print(len(Arr))
    Arr.append(3)
    print(Arr[2])
    print(len(Arr))
    print(Arr.pop())
    print(Arr[0], Arr[1])
    print(len(Arr))
    Arr.insert(0, 5)
    print(Arr[0], Arr[1], Arr[2])
    Arr.pop(0)
    print(Arr[0], Arr[1], Arr[2])
    Arr[1] = 100
    print(Arr[1])