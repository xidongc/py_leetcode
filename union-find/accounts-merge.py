class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        mail_to_index = dict()
        self.fa = dict()
        for i, account in enumerate(accounts):
            if len(account) > 1:
                for mail in account[1:]:
                    if mail not in self.fa:
                        self.fa[mail] = mail
                        mail_to_index[mail] = i
                    self.Union(mail, account[1])
        index_to_mails = dict()
        for mail in mail_to_index.keys():
            fmail = self.Find(mail)
            findex = mail_to_index[fmail]
            if findex not in index_to_mails:
                index_to_mails[findex] = [mail]
            else:
                index_to_mails[findex].append(mail)
        ret = []
        for index, mails in index_to_mails.items():
            l = [accounts[index][0]]
            l.extend(sorted(mails))
            ret.append(l)
        return ret

    def Union(self, x, y):
        fx, fy = self.Find(x), self.Find(y)
        if fx != fy:
            self.fa[fx] = fy

    def Find(self, x):
        p = x
        while p != self.fa[p]:
            p = self.fa[p]
        while x != self.fa[x]:
            t = self.fa[x]
            self.fa[x] = p
            x = t
        return p

# from xidong

class Solution(object):

    def __init__(self):
        self.father = dict()

    def accountsMerge(self, accounts):

        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        email_to_name = dict()
        result = list()
        ret = dict()

        if not accounts or len(accounts) < 1:
            return []

        for account in accounts:
            if len(account) > 1:
                name = account[0]
                emails = account[1:]
                for email in emails:
                    if email not in self.father.keys():
                        self.father[email] = email
                        self.union(email, emails[0])
                    else:
                        root = self.find(email)
                        self.union(emails[0], root)
                email_to_name[emails[0]] = name

        for email, name in email_to_name.items():
            ret[email] = []
        for email in self.father.keys():
            root = self.find(email)
            ret[root].append(email)

        for key, val in ret.items():
            if len(val) >= 1:
                val.sort()
                tmp = [email_to_name[key]]
                tmp.extend(val)
                result.append(tmp)
        print(result)
        return result

    def find(self, email):
        if email == self.father[email]:
            return email

        self.father[email] = self.find(self.father[email])
        return self.father[email]

    def union(self, email_1, email_2):
        root_1 = self.find(email_1)
        root_2 = self.find(email_2)
        if root_1 != root_2:
            self.father[root_1] = root_2
        else:
            return root_1

# test

accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
s = Solution()
s.accountsMerge(accounts)

print([["John", "john00@mail.com", "john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])

