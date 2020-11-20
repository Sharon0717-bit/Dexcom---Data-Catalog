__author__ = "Thomas McGinn"
__credits__ = ["Thomas McGinn"]
__version__ = "0.0.0"
__maintainer__ = "Thomas McGinn"
__email__ = "thomas.mcginn@dexcom.com"
__status__ = "Production"

from search import Search
import utilities as u

class Clarity(Search):
    def __init__(self):
        super().__init__()
        self.title = ['Clarity']
        self.Path_ = [r'Z:\QA\Data Analysis\Clarity']
        self.Parent_landing_page_path = ['#']
        self.Landing_page_path = ['#']
        self.Repository_path = [r'C:\Users\[username]\Desktop\Customer-Advocacy-Searches/blob/master/Library/Complaints/clarity.py']
        self.Github_repository_path = [r'https://github.com/dexcom-inc/Customer-Advocacy-Searches/blob/master/Library/Complaints/clarity.py']
        self.Short_description = ['Testing Data']
        self.Long_description = ['#']
        self.Long_description_html = ['#']
        self.Technical_description = ['#']
        self.Databases_used = ['customer_advocacy_pms']
        self.Technical_databases_used = ['#']
        self.Created_by = [__author__]
        self.Maintained_by = [__maintainer__]
        self.Maintained_by_backup = ['#']


