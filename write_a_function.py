if __name__ == "__main__":
    year = int(input())
    def is_leap(years):
        if years % 4 == 0:
            if years % 100 != 0:
                return True
            elif years % 400 == 0:
                return True
        return False

    print(is_leap(year))