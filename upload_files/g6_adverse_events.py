__author__ = "Christopher Stetzer"
__credits__ = ["Christopher Stetzer"]
__maintainer__ = "cs0819"
__email__ = "christopher.stetzer@dexcom.com"

from search import Search
import utilities as u

class G6_Adverse(Search):
    def __init__(self):
        super().__init__()
        self.title = ['G6_Adverse_Events'.lower()]
        self.Path_ = [r'Z:\QA\Data Analysis\G6 Adverse Events']
        self.Parent_landing_page_path = ['#']
        self.Landing_page_path = ['#']
        self.Repository_path = [r'C:\Users\[username]\Desktop\Customer-Advocacy-Searches/blob/master/Library/Complaints/g6_adverse_events.py']
        self.Github_repository_path = [r'https://github.com/dexcom-inc/Customer-Advocacy-Searches/blob/master/Library/Complaints/g6_adverse_events.py']
        self.Short_description = ['Pulls G6 Adverse Event complaints from the past week']
        self.Long_description = ['#']
        self.Long_description_html = ['#']
        self.Technical_description = ['#']
        self.Databases_used = ['customer_advocacy_pms']
        self.Technical_databases_used = ['#']
        self.Created_by = [__author__]
        self.Maintained_by = [__maintainer__]
        self.Maintained_by_backup = ['#']

# title = ''.join(G6_Adverse().title)
# Path_ = ''.join(G6_Adverse().Path_)
# Path_ = Path_.replace('\\', '\\\\')
# Parent_landing_page_path = ''.join(G6_Adverse().Parent_landing_page_path)
# Parent_landing_page_path = Parent_landing_page_path.replace('\\', '\\\\')
# Landing_page_path = ''.join(G6_Adverse().Landing_page_path)
# Landing_page_path = Landing_page_path.replace('\\', '\\\\')
# Repository_path = ''.join(G6_Adverse().Repository_path)
# Repository_path = Repository_path.replace('\\', '\\\\')
# Github_repository_path = ''.join(G6_Adverse().Github_repository_path)
# Short_description = ''.join(G6_Adverse().Short_description)
# Long_description = ''.join(G6_Adverse().Long_description)
# Long_description_html = ''.join(G6_Adverse().Long_description_html)
# Technical_description = ''.join(G6_Adverse().Technical_description)
# Databases_used = ''.join(G6_Adverse().Databases_used)
# Technical_databases_used = ''.join(G6_Adverse().Technical_databases_used)
# Created_by = ''.join(G6_Adverse().Created_by)
# Maintained_by = ''.join(G6_Adverse().Maintained_by)
# Maintained_by_backup = ''.join(G6_Adverse().Maintained_by_backup)


# u.upload_doc_string_to_mysql(title, Path_, Parent_landing_page_path, Landing_page_path, Repository_path, Github_repository_path, Short_description, Long_description, Long_description_html, Technical_description, Databases_used, Technical_databases_used, Created_by, Maintained_by, Maintained_by_backup)
