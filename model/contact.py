from sys import maxsize


class Contact:

    def __init__(self, fName=None, lName=None, title=None, company=None, address_1=None, hPhone=None,
                 mPhone=None, email=None, bDay=None, bMonth=None, bYear=None,
                 address_2=None, notes=None, homepage=None, id=None):
        self.fName = fName
        self.lName = lName
        self.title = title
        self.company = company
        self.address_1 = address_1
        self.hPhone = hPhone
        self.mPhone = mPhone
        self.email = email
        self.bDay = bDay
        self.bMonth = bMonth
        self.bYear = bYear
        self.address_2 = address_2
        self.notes = notes
        self.homepage = homepage
        self.id = id

    def __repr__(self):
        return "$s:$s" % (self.id, self.fName)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.fName == other.fName

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
