__author__ = "Thomas McGinn"
__credits__ = ["Thomas McGinn"]
__version__ = "0.0.5"
__maintainer__ = "Thomas McGinn"
__email__ = "thomas.mcginn@dexcom.com"
__status__ = "Production"

from search import Search
import utilities as u

class Follow_App(Search):
    def __init__(self):
        super().__init__()
        self.title = ['follow_app']
        self.Path_ = [r'Z:\QA\Data Analysis\Follow App']
        self.Parent_landing_page_path = ['#']
        self.Landing_page_path = ['#']
        self.Repository_path = [r'C:\Users\[username]\Desktop\Customer-Advocacy-Searches/blob/master/Library/Complaints/follow_app.py']
        self.Github_repository_path = [r'https://github.com/dexcom-inc/Customer-Advocacy-Searches/blob/master/Library/Complaints/follow_app.py']
        self.Short_description = ['Testing Data']
        self.Long_description = ['#']
        self.Long_description_html = ['#']
        self.Technical_description = ['#']
        self.Databases_used = ['customer_advocacy_pms']
        self.Technical_databases_used = ['#']
        self.Created_by = [__author__]
        self.Maintained_by = [__maintainer__]
        self.Maintained_by_backup = ['#']

# title = ''.join(Follow_App().title)
# Path_ = ''.join(Follow_App().Path_)
# Path_ = Path_.replace('\\', '\\\\')
# Parent_landing_page_path = ''.join(Follow_App().Parent_landing_page_path)
# Parent_landing_page_path = Parent_landing_page_path.replace('\\', '\\\\')
# Landing_page_path = ''.join(Follow_App().Landing_page_path)
# Landing_page_path = Landing_page_path.replace('\\', '\\\\')
# Repository_path = ''.join(Follow_App().Repository_path)
# Repository_path = Repository_path.replace('\\', '\\\\')
# Github_repository_path = ''.join(Follow_App().Github_repository_path)
# Short_description = ''.join(Follow_App().Short_description)
# Long_description = ''.join(Follow_App().Long_description)
# Long_description_html = ''.join(Follow_App().Long_description_html)
# Technical_description = ''.join(Follow_App().Technical_description)
# Databases_used = ''.join(Follow_App().Databases_used)
# Technical_databases_used = ''.join(Follow_App().Technical_databases_used)
# Created_by = ''.join(Follow_App().Created_by)
# Maintained_by = ''.join(Follow_App().Maintained_by)
# Maintained_by_backup = ''.join(Follow_App().Maintained_by_backup)


# u.upload_doc_string_to_mysql(title, Path_, Parent_landing_page_path, Landing_page_path, Repository_path, Github_repository_path, Short_description, Long_description, Long_description_html, Technical_description, Databases_used, Technical_databases_used, Created_by, Maintained_by, Maintained_by_backup)


