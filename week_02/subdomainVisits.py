from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        result = []
        domain_dict = dict()
        for domain in cpdomains:
            count = int(domain.split(" ")[0])
            sub_domain_list = domain.split(" ")[1].split('.')
            sub_domain = ''
            for i in range(len(sub_domain_list)-1, -1, -1):
                sub_domain = sub_domain_list[i] + '.' + sub_domain
                sub_domain = sub_domain.rstrip(".")
                if sub_domain in domain_dict:
                    domain_dict[sub_domain] += count
                else:
                    domain_dict[sub_domain] = count
        for key, value in domain_dict.items():
            result.append(str(value) + ' ' + key)
        return result
