__author__ = "Thomas McGinn"
__credits__ = ["Thomas McGinn"]
__version__ = "0.0.5"
__maintainer__ = "Thomas McGinn"
__email__ = "thomas.mcginn@dexcom.com"
__status__ = "Production"

from search import Search
import utilities as u

class G6_14_Day(Search):
    def __init__(self):
        super().__init__()
        self.title = ['G6_14_Day'.lower()]
        self.Path_ = [r'Z:\QA\Data Analysis\G6 14 Day']
        self.Parent_landing_page_path = ['#']
        self.Landing_page_path = ['#']
        self.Repository_path = [r'C:\Users\[username]\Desktop\Customer-Advocacy-Searches/blob/master/Library/Complaints/g6_14_day.py']
        self.Github_repository_path = [r'https://github.com/dexcom-inc/Customer-Advocacy-Searches/blob/master/Library/Complaints/g6_14_day.py']
        self.Short_description = ['Testing Data']
        self.Long_description = ['#']
        self.Long_description_html = ['#']
        self.Technical_description = ['#']
        self.Databases_used = ['customer_advocacy_pms']
        self.Technical_databases_used = ['#']
        self.Created_by = [__author__]
        self.Maintained_by = [__maintainer__]
        self.Maintained_by_backup = ['#']

# title = ''.join(G6_14_Day().title)
# Path_ = ''.join(G6_14_Day().Path_)
# Path_ = Path_.replace('\\', '\\\\')
# Parent_landing_page_path = ''.join(G6_14_Day().Parent_landing_page_path)
# Parent_landing_page_path = Parent_landing_page_path.replace('\\', '\\\\')
# Landing_page_path = ''.join(G6_14_Day().Landing_page_path)
# Landing_page_path = Landing_page_path.replace('\\', '\\\\')
# Repository_path = ''.join(G6_14_Day().Repository_path)
# Repository_path = Repository_path.replace('\\', '\\\\')
# Github_repository_path = ''.join(G6_14_Day().Github_repository_path)
# Short_description = ''.join(G6_14_Day().Short_description)
# Long_description = ''.join(G6_14_Day().Long_description)
# Long_description_html = ''.join(G6_14_Day().Long_description_html)
# Technical_description = ''.join(G6_14_Day().Technical_description)
# Databases_used = ''.join(G6_14_Day().Databases_used)
# Technical_databases_used = ''.join(G6_14_Day().Technical_databases_used)
# Created_by = ''.join(G6_14_Day().Created_by)
# Maintained_by = ''.join(G6_14_Day().Maintained_by)
# Maintained_by_backup = ''.join(G6_14_Day().Maintained_by_backup)


# u.upload_doc_string_to_mysql(title, Path_, Parent_landing_page_path, Landing_page_path, Repository_path, Github_repository_path, Short_description, Long_description, Long_description_html, Technical_description, Databases_used, Technical_databases_used, Created_by, Maintained_by, Maintained_by_backup)


