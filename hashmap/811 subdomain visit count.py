import collections
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domainDict = collections.defaultdict(int)
        for domains in cpdomains:
            count, domains = domains.split(' ')
            count = int(count)
            domainList = self.getParentDomains(domains)
            for domain in domainList:
                domainDict[domain] += count
        return [str(domainDict[domain]) + ' ' + domain for domain in domainDict]
    def getParentDomains(self, domains):
        domainList = [domains]
        counts = domains.count('.')
        for i in range(counts):
            pos = domains.index('.')
            domains = domains[pos+1:]
            domainList.append(domains)
        return domainList