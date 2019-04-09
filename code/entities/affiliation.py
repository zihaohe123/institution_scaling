# definition of the affiliation entity of MAG data
class Affiliation:
    def __init__(self, affId, aff_name):

        # basic information of an affiliation
        self.affId = affId
        self.aff_name = aff_name

        # properties related to affiliation size
        self.year_paperId_authorIds = {}
        self.year_authorIds = {}
        self.year_size = {}
        self.year_cumul_authorIds = {} # cumulative authorIds up to that year
        self.year_cumul_size = {}   # cumulative size up to that year

        # properties related to collaborations
        self.year_paperId_internal_collab = {}
        self.year_paperId_external_inst_collab = {}
        self.year_paperId_external_indiv_collab = {}
        self.year_paperId_indiv_collab = {}
        self.year_internal_collab = {}
        self.year_external_inst_collab = {}
        self.year_external_indiv_collab = {}
        self.year_indiv_collab = {}  # internal (individual) collaborations + external individual collaborations
        self.year_cumul_internal_collab = {}
        self.year_cumul_external_inst_collab = {}
        self.year_cumul_external_indiv_collab = {}
        self.year_cumul_indiv_collab = {}
        self.year_avg_internal_collab = {}
        self.year_avg_external_inst_collab = {}
        self.year_avg_external_indiv_collab = {}
        self.year_avg_indiv_collab = {}

        # properties related to production and productivity
        self.year_production = {}
        self.year_paperId_contribution = {}
        self.year_productivity = {}
        self.year_cumul_production = {}
        self.year_cumul_productivity = {}

        # properties related to team size
        self.year_paperId_teamsize = {}
        self.year_paperId_internal_teamsize = {}
        self.year_paperId_external_teamsize = {}
        self.year_avg_teamsize = {}
        self.year_avg_internal_teamsize = {}
        self.year_avg_external_teamsize = {}

        # properties related to the overall citations and average impact
        self.year_paperId_citations = {}
        self.year_citations = {}
        self.year_avg_impact = {}

        # properties related to citations and average impact from one-author papers
        self.year_paperId_citations_oneauthor = {}
        self.year_citations_oneauthor = {}
        self.year_avg_impact_oneauthor = {}

        # properties related to citations and average impact from two-author papers
        self.year_paperId_citations_twoauthor = {}
        self.year_citations_twoauthor = {}
        self.year_avg_impact_twoauthor = {}

        # properties related to citations and average impact from three-author papers
        self.year_paperId_citations_threeauthor = {}
        self.year_citations_threeauthor = {}
        self.year_avg_impact_threeauthor = {}

        # properties related to citations and average impact from one-and-two-author papers
        self.year_paperId_citations_onetwoauthor = {}
        self.year_citations_onetwoauthor = {}
        self.year_avg_impact_onetwoauthor = {}

        # properties related to citations and average impact from three-to-six-author papers
        self.year_paperId_citations_three2sixauthor = {}
        self.year_citations_three2sixauthor = {}
        self.year_avg_impact_three2sixauthor = {}

        # this parameter is used to index the property
        self.propertyname_property = {}

    def add_paper(self, year, authorIds, paperId, contribution, teamsize, internal_teamsize, external_teamsize,
                  citations, internal_collab, external_inst_collab, external_indiv_collab,indiv_collab):
        """
        add a paper and update the concerning properties
        :param year: publication year
        :param authorIds:
        :param paperId:
        :param contribution:
        :param teamsize:
        :param internal_teamsize:
        :param external_teamsize:
        :param citations:
        :param internal_collab:
        :param external_inst_collab:
        :param external_indiv_collab:
        :param indiv_collab:
        :return:
        """

        # paperId and its authorIds
        if year not in self.year_paperId_authorIds:
            self.year_paperId_authorIds[year] = {}
        if paperId not in self.year_paperId_authorIds[year]:
            self.year_paperId_authorIds[year][paperId] = set()
        for authorId in authorIds:
            self.year_paperId_authorIds[year][paperId].add(authorId)

        # production and productivity
        if year not in self.year_paperId_contribution:
            self.year_paperId_contribution[year] = {}
        self.year_paperId_contribution[year][paperId] = contribution

        # paperId and teamsize
        if year not in self.year_paperId_teamsize:
            self.year_paperId_teamsize[year] = {}
        self.year_paperId_teamsize[year][paperId] = teamsize
        if year not in self.year_paperId_internal_teamsize:
            self.year_paperId_internal_teamsize[year] = {}
        self.year_paperId_internal_teamsize[year][paperId] = internal_teamsize
        if year not in self.year_paperId_external_teamsize:
            self.year_paperId_external_teamsize[year] = {}
        self.year_paperId_external_teamsize[year][paperId] = external_teamsize

        # collaborations
        if year not in self.year_paperId_internal_collab:
            self.year_paperId_internal_collab[year] = {}
        self.year_paperId_internal_collab[year][paperId] = internal_collab

        if year not in self.year_paperId_external_inst_collab:
            self.year_paperId_external_inst_collab[year] = {}
        self.year_paperId_external_inst_collab[year][paperId] = external_inst_collab
        if year not in self.year_paperId_external_indiv_collab:
            self.year_paperId_external_indiv_collab[year] = {}
        self.year_paperId_external_indiv_collab[year][paperId] = external_indiv_collab
        if year not in self.year_paperId_indiv_collab:
            self.year_paperId_indiv_collab[year] = {}
        self.year_paperId_indiv_collab[year][paperId] = indiv_collab

        # citations
        if year not in self.year_paperId_citations:
            self.year_paperId_citations[year] = {}
        self.year_paperId_citations[year][paperId] = citations

        # one-author paper citations
        if len(authorIds) == 1:
            if year not in self.year_paperId_citations_oneauthor:
                self.year_paperId_citations_oneauthor[year] = {}
            self.year_paperId_citations_oneauthor[year][paperId] = citations

        # two-author paper citations
        if len(authorIds) == 2:
            if year not in self.year_paperId_citations_twoauthor:
                self.year_paperId_citations_twoauthor[year] = {}
            self.year_paperId_citations_twoauthor[year][paperId] = citations

        # three-author paper citations
        if len(authorIds) == 3:
            if year not in self.year_paperId_citations_threeauthor:
                self.year_paperId_citations_threeauthor[year] = {}
            self.year_paperId_citations_threeauthor[year][paperId] = citations

        # one-and-two-author paper citations
        if len(authorIds) in [1, 2]:
            if year not in self.year_paperId_citations_onetwoauthor:
                self.year_paperId_citations_onetwoauthor[year] = {}
            self.year_paperId_citations_onetwoauthor[year][paperId] = citations

        # three-to-six-author paper citations
        if len(authorIds) in [3, 4, 5, 6]:
            if year not in self.year_paperId_citations_three2sixauthor:
                self.year_paperId_citations_three2sixauthor[year] = {}
            self.year_paperId_citations_three2sixauthor[year][paperId] = citations

    def update_affiliation(self):
        """
        paper-specific properties --> affiliation-specific properties
        :return:
        """

        # authorIds and size
        for year in self.year_paperId_authorIds:
            self.year_authorIds[year] = set()
            for paperId in self.year_paperId_authorIds[year]:
                authorIds = self.year_paperId_authorIds[year][paperId]
                self.year_authorIds[year] = self.year_authorIds[year].union(authorIds)
            self.year_size[year] = len(self.year_authorIds[year])

        # cumulative authorIds and size
        years = list(self.year_size.keys())
        years.sort()
        first_year = years[0]
        self.year_cumul_authorIds[first_year] = set(self.year_authorIds[first_year])
        for i in range(1, len(years)):
            cur_year = years[i]
            prev_year = years[i-1]
            self.year_cumul_authorIds[cur_year] = self.year_cumul_authorIds[prev_year].union(set(self.year_authorIds[cur_year]))
        for year in self.year_cumul_authorIds:
            self.year_cumul_size[year] = len(self.year_cumul_authorIds[year])

        # internal collaborations
        for year in self.year_paperId_internal_collab:
            self.year_internal_collab[year] = set()
            for paperId in self.year_paperId_internal_collab[year]:
                internal_collab = self.year_paperId_internal_collab[year][paperId]
                self.year_internal_collab[year] = self.year_internal_collab[year].union(internal_collab)
        years = list(self.year_internal_collab.keys())
        years.sort()
        first_year = years[0]
        self.year_cumul_internal_collab[first_year] = self.year_internal_collab[first_year]
        for i in range(1, len(years)):
            cur_year = years[i]
            prev_year = years[i-1]
            self.year_cumul_internal_collab[cur_year] = self.year_cumul_internal_collab[prev_year].union(self.year_internal_collab[cur_year])
        for year in self.year_internal_collab:
            self.year_internal_collab[year] = len(self.year_internal_collab[year]) // 2
            self.year_cumul_internal_collab[year] = len(self.year_cumul_internal_collab[year]) // 2
            self.year_avg_internal_collab[year] = self.year_internal_collab[year] / self.year_size[year]

        # external institutional collaborations
        for year in self.year_paperId_external_inst_collab:
            self.year_external_inst_collab[year] = set()
            for paperId in self.year_paperId_internal_collab[year]:
                external_inst_collab = self.year_paperId_external_inst_collab[year][paperId]
                self.year_external_inst_collab[year] = self.year_external_inst_collab[year].union(external_inst_collab)
        years = list(self.year_external_inst_collab.keys())
        years.sort()
        first_year = years[0]
        self.year_cumul_external_inst_collab[first_year] = self.year_external_inst_collab[first_year]
        for i in range(1, len(years)):
            cur_year = years[i]
            prev_year = years[i-1]
            self.year_cumul_external_inst_collab[cur_year] = self.year_cumul_external_inst_collab[prev_year].union(self.year_external_inst_collab[cur_year])
        for year in self.year_external_inst_collab:
            self.year_external_inst_collab[year] = len(self.year_external_inst_collab[year])
            self.year_cumul_external_inst_collab[year] = len(self.year_cumul_external_inst_collab[year])
            self.year_avg_external_inst_collab[year] = self.year_external_inst_collab[year] / self.year_size[year]

        # external individual collaborations
        for year in self.year_paperId_external_indiv_collab:
            self.year_external_indiv_collab[year] = set()
            for paperId in self.year_paperId_external_indiv_collab[year]:
                external_indiv_collab = self.year_paperId_external_indiv_collab[year][paperId]
                self.year_external_indiv_collab[year] = self.year_external_indiv_collab[year].union(external_indiv_collab)
        years = list(self.year_external_indiv_collab.keys())
        years.sort()
        first_year = years[0]
        self.year_cumul_external_indiv_collab[first_year] = self.year_external_indiv_collab[first_year]
        for i in range(1, len(years)):
            cur_year = years[i]
            prev_year = years[i-1]
            self.year_cumul_external_indiv_collab[cur_year] = self.year_cumul_external_indiv_collab[prev_year].union(self.year_external_indiv_collab[cur_year])
        for year in self.year_external_indiv_collab:
            self.year_external_indiv_collab[year] = len(self.year_external_indiv_collab[year]) // 2
            self.year_cumul_external_indiv_collab[year] = len(self.year_cumul_external_indiv_collab[year]) // 2
            self.year_avg_external_indiv_collab[year] = self.year_external_indiv_collab[year] / self.year_size[year]

        # individual collaborations
        for year in self.year_paperId_indiv_collab:
            self.year_indiv_collab[year] = set()
            for paperId in self.year_paperId_indiv_collab[year]:
                indiv_collab = self.year_paperId_indiv_collab[year][paperId]
                self.year_indiv_collab[year] = self.year_indiv_collab[year].union(indiv_collab)
        years = list(self.year_indiv_collab.keys())
        years.sort()
        first_year = years[0]
        self.year_cumul_indiv_collab[first_year] = self.year_indiv_collab[first_year]
        for i in range(1, len(years)):
            cur_year = years[i]
            prev_year = years[i-1]
            self.year_cumul_indiv_collab[cur_year] = self.year_cumul_indiv_collab[prev_year].union(self.year_indiv_collab[cur_year])
        for year in self.year_indiv_collab:
            self.year_indiv_collab[year] = len(self.year_indiv_collab[year]) // 2
            self.year_cumul_indiv_collab[year] = len(self.year_cumul_indiv_collab[year]) // 2
            self.year_avg_indiv_collab[year] = self.year_indiv_collab[year] / self.year_size[year]

        # production and productivity
        for year in self.year_paperId_authorIds:
            self.year_production[year] = len(self.year_paperId_authorIds[year])
        for year in self.year_paperId_contribution:
            self.year_productivity[year] = sum(self.year_paperId_contribution[year].values())
        years = list(self.year_production)
        years.sort()
        first_year = years[0]
        self.year_cumul_production[first_year] = self.year_production[first_year]
        self.year_cumul_productivity[first_year] = self.year_productivity[first_year]
        for i in range(1, len(years)):
            cur_year = years[i]
            prev_year = years[i-1]
            self.year_cumul_production[cur_year] = self.year_cumul_production[prev_year] + self.year_production[cur_year]
            self.year_cumul_productivity[cur_year] = self.year_cumul_productivity[prev_year] + self.year_productivity[cur_year]

        # teamsize
        for year in self.year_paperId_teamsize:
            self.year_avg_teamsize[year] = sum(self.year_paperId_teamsize[year].values()) / len(self.year_paperId_teamsize[year])
        for year in self.year_paperId_internal_teamsize:
            self.year_avg_internal_teamsize[year] = sum(self.year_paperId_internal_teamsize[year].values()) / len(self.year_paperId_internal_teamsize[year])
        for year in self.year_paperId_external_teamsize:
            self.year_avg_external_teamsize[year] = sum(self.year_paperId_external_teamsize[year].values()) / len(self.year_paperId_external_teamsize[year])

        # citations and average impact
        for year in self.year_paperId_citations:
            self.year_citations[year] = sum(self.year_paperId_citations[year].values())
        for year in self.year_citations:
            self.year_avg_impact[year] = 0 if len(self.year_citations) == 0 \
                else self.year_citations[year] / len(self.year_paperId_citations[year])

        # citations and average impact of one-author papers
        for year in self.year_paperId_citations_oneauthor:
            self.year_citations_oneauthor[year] = sum(self.year_paperId_citations_oneauthor[year].values())
        for year in self.year_citations_oneauthor:
            self.year_avg_impact_oneauthor[year] = 0 if len(self.year_citations_oneauthor) == 0 \
                else self.year_citations_oneauthor[year] / len(self.year_paperId_citations_oneauthor[year])

        # citations and average impact of two-author papers
        for year in self.year_paperId_citations_twoauthor:
            self.year_citations_twoauthor[year] = sum(self.year_paperId_citations_twoauthor[year].values())
        for year in self.year_citations_twoauthor:
            self.year_avg_impact_twoauthor[year] = 0 if len(self.year_citations_twoauthor) == 0 \
                else self.year_citations_twoauthor[year] / len(self.year_paperId_citations_twoauthor[year])

        # citations and average impact of three-author papers
        for year in self.year_paperId_citations_threeauthor:
            self.year_citations_threeauthor[year] = sum(self.year_paperId_citations_threeauthor[year].values())

        for year in self.year_citations_threeauthor:
            self.year_avg_impact_threeauthor[year] = 0 if len(self.year_citations_threeauthor) == 0 \
                else self.year_citations_threeauthor[year] / len(self.year_paperId_citations_threeauthor[year])

        # citations and average impact of one-and-two-author papers
        for year in self.year_paperId_citations_onetwoauthor:
            self.year_citations_onetwoauthor[year] = sum(self.year_paperId_citations_onetwoauthor[year].values())
        for year in self.year_citations_onetwoauthor:
            self.year_avg_impact_onetwoauthor[year] = 0 if len(self.year_citations_onetwoauthor) == 0 \
                else self.year_citations_onetwoauthor[year] / len(self.year_paperId_citations_onetwoauthor[year])

        # citations and average impact of three-to-six-author papers
        for year in self.year_paperId_citations_three2sixauthor:
            self.year_citations_three2sixauthor[year] = sum(self.year_paperId_citations_three2sixauthor[year].values())
        for year in self.year_citations_three2sixauthor:
            self.year_avg_impact_three2sixauthor[year] = 0 if len(self.year_citations_three2sixauthor) == 0 \
                else self.year_citations_three2sixauthor[year] / len(self.year_paperId_citations_three2sixauthor[year])

        # release the memory of paper-specific properties that will not be used anymore
        self.year_paperId_authorIds = {}
        self.year_cumul_authorIds = {}
        self.year_authorIds = {}
        self.year_paperId_contribution = {}
        self.year_paperId_teamsize = {}
        self.year_paperId_internal_teamsize = {}
        self.year_paperId_external_teamsize = {}
        self.year_paperId_internal_collab = {}
        self.year_paperId_external_inst_collab = {}
        self.year_paperId_external_indiv_collab = {}
        self.year_paperId_indiv_collab = {}
        self.year_paperId_citations = {}
        self.year_paperId_citations_oneauthor = {}
        self.year_paperId_citations_twoauthor = {}
        self.year_paperId_citations_threeauthor = {}
        self.year_paperId_citations_onetwoauthor = {}
        self.year_paperId_citations_three2sixauthor = {}

        self.propertyname_property = {
            'size': self.year_size,
            'cumul_size': self.year_cumul_size,
            'internal_collab': self.year_internal_collab,
            'external_inst_collab': self.year_external_inst_collab,
            'external_indiv_collab': self.year_external_indiv_collab,
            'indiv_collab': self.year_indiv_collab,
            'cumul_internal_collab': self.year_cumul_internal_collab,
            'cumul_external_inst_collab': self.year_cumul_external_inst_collab,
            'cumul_external_indiv_collab': self.year_cumul_external_indiv_collab,
            'cumul_indiv_collab': self.year_indiv_collab,
            'avg_internal_collab': self.year_avg_internal_collab,
            'avg_external_inst_collab': self.year_avg_external_inst_collab,
            'avg_external_indiv_collab': self.year_avg_external_indiv_collab,
            'avg_indiv_collab': self.year_avg_indiv_collab,
            'production': self.year_production,
            'productivity': self.year_productivity,
            'avg_teamsize': self.year_avg_teamsize,
            'avg_internal_teamsize': self.year_avg_internal_teamsize,
            'avg_external_teamsize': self.year_avg_external_teamsize,
            'avg_impact': self.year_avg_impact,
            'avg_impact_oneauthor': self.year_avg_impact_oneauthor,
            'avg_impact_twoauthor': self.year_avg_impact_twoauthor,
            'avg_impact_threeauthor': self.year_avg_impact_threeauthor,
            'avg_impact_onetwoauthor': self.year_avg_impact_onetwoauthor,
            'avg_impact_three2sizeauthor': self.year_avg_impact_three2sixauthor,
        }
