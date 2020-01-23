class Month:
    def __init__(self, year, month_num):
        self.year = year
        self.month_num = month_num

    def __repr__(self):
        return (self.year, self.month_num)

    def __str__(self):
        return f"{self.year}-{self.month_num}"

    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif other.year < self.year:
            return False
        elif self.year == other.year and self.month_num < other.month_num:
            return True
        else:
            return False





if __name__ == '__main__':
    pass
