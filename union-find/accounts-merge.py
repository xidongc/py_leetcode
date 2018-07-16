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

