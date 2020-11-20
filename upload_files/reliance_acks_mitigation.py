__author__ = "Jesse Mak"
__credits__ = ["Jesse Mak","Thomas McGinn"]
__version__ = "0.0.1"
__maintainer__ = "Thomas McGinn"
__email__ = "thomas.mcginn@dexcom.com"
__status__ = "Production"

from search import Search
import utilities as u

class Reliance_Acks_Mitigation(Search):
    def __init__(self):
        super().__init__()
        self.title = ['reliance_acks_mitigation']
        self.Path_ = [r'Z:\QA\Data Analysis\Reliance ACKs Mitigation']
        self.Parent_landing_page_path = ['#']
        self.Landing_page_path = [r'file:///Z:/QA/Customer%20Returns-Complaint%20System/Thomas-Jesse/Searches/Mitigations/main.html']
        self.Repository_path = [r'C:\Users\[username]\Desktop\Customer-Advocacy-Searches\Library\Mitigations\reliance_acks_mitigation.py']
        self.Github_repository_path = [r'https://github.com/dexcom-inc/Customer-Advocacy-Searches/blob/master/Library/Mitigations/reliance_acks_mitigation.py']
        self.Short_description = ['Reliance ACKs Mitigation for Customer Advocacy']
        self.Long_description = ['This is a daily report of complaints in Reliance. This excel file containts the following sheets: 1. ACKs Mitig - This is a list of complaints where a decision has been made and no MedWatch has been submitted or a MedWatch has been submitted, but the third_acknowledgement failed. 2. Not Complete - This is a list of reportable and potentially reportable complaints where a decision has not been made yet OR medical intervention or death is marked as Yes. Additionally it checks if the medwatch exists OR if the medwatch has not been submitted or not completed. And it also makes sure the complaint is not completed or voided. 3. Potential Supps-Upgrades - This is a list of complaints that require a supplemental or the complaint has been upgraded, requiring a submission of the initial MedWatch.']
        self.Long_description_html = ['This is a daily report of complaints in Reliance. This excel file containts the following sheets:'
                            +'<ul style="list-style-type:circle;font-size:14px">'
                            +    '<li>ACKs Mitig:'
                            +        '<ul style="list-style-type:square;font-size:12px">'
                            +            '<li>This is a list of complaints where a decision has been made and no MedWatch has been submitted or a MedWatch has been submitted, but the third_acknowledgement failed.</li>'
                            +        '</ul>'
                            +     '</li>'
                            +    '<li>Not Complete:'
                            +        '<ul style="list-style-type:square;font-size:12px">'
                            +             '<li>This is a list of reportable and potentially reportable complaints where a decision has not been made yet OR medical intervention or death is marked as Yes. Additionally it checks if the medwatch exists OR if the medwatch has not been submitted or not completed. And it also makes sure the complaint is not completed or voided.</li>'
                            +        '</ul>'
                            +     '</li>'
                            +    '<li>Potential Supps-Upgrades:'
                            +        '<ul style="list-style-type:square;font-size:12px">'
                            +             '<li>This is a list of complaints that require a supplemental or the complaint has been upgraded, requiring a submission of the initial MedWatch</li>'
                            +        '</ul>'
                            +     '</li>'
                            +'</ul>'
                            +'<br>Data: Reliance Only']
        self.Technical_description = ["Each sheet in this report has it's own function as well as the supporting functions that actually run those functions and generate the report. The write_output function is what is called in the main script.py. It starts by creating the shortcut to the path of the report and generates that shortcut in the Shortcuts Folder. Then, it runs eah of the functions (3) to generate the dataframes needed for the sheets and report. By default, the multiprocessing_flag is false stating that it will write the report individually using the write_individually function. This is defaulted to False as the main script.py is already running on a multiprocess and hence cannot create more child processes off of a child process. If True, it will run each of the functions in a multiprocess to generate the excel sheets quicker. Afterward, it 1. moves yesterdays report to the appropriate folder in the Z Drive, 2. uploads the report sharepoint and moves yesterdays report to the appropriate folder in Sharepoint, 3. writes the html list to sharepoint so that the sharepoint site is now linked to the new report location by using the sharepoint list 'acks mitigation', 4. it uploads all the mitigation results to the database under the mitigations tables for each of the excel sheets."]
        self.Databases_used = ['Reliance Only']
        self.Technical_databases_used = ['customer_advocacy_reliance','reliance-prod']
        self.Created_by = [__author__]
        self.Maintained_by = [__maintainer__]
        self.Maintained_by_backup = ['tm0616','jmak']

# title = ''.join(Reliance_Acks_Mitigation().title)
# Path_ = ''.join(Reliance_Acks_Mitigation().Path_)
# Path_ = Path_.replace('\\', '\\\\')
# Parent_landing_page_path = ''.join(Reliance_Acks_Mitigation().Parent_landing_page_path)
# Parent_landing_page_path = Parent_landing_page_path.replace('\\', '\\\\')
# Landing_page_path = ''.join(Reliance_Acks_Mitigation().Landing_page_path)
# Landing_page_path = Landing_page_path.replace('\\', '\\\\')
# Landing_page_path = Landing_page_path.replace('%20', ' ')
# Repository_path = ''.join(Reliance_Acks_Mitigation().Repository_path)
# Repository_path = Repository_path.replace('\\', '\\\\')
# Github_repository_path = ''.join(Reliance_Acks_Mitigation().Github_repository_path)
# Short_description = ''.join(Reliance_Acks_Mitigation().Short_description)
# Long_description = ''.join(Reliance_Acks_Mitigation().Long_description)
# Long_description = Long_description.replace("'", "\\'")
# Long_description_html = ''.join(Reliance_Acks_Mitigation().Long_description_html)
# Long_description_html = Long_description_html.replace('\\', '\\\\')
# Long_description_html = Long_description_html.replace("'", "\\'")
# Long_description_html = Long_description_html.replace('"', '\\"')
# Technical_description = ''.join(Reliance_Acks_Mitigation().Technical_description)
# Technical_description = Technical_description.replace("'", "\\'")
# Databases_used = ''.join(Reliance_Acks_Mitigation().Databases_used)
# Technical_databases_used = ','.join(Reliance_Acks_Mitigation().Technical_databases_used)
# Created_by = ''.join(Reliance_Acks_Mitigation().Created_by)
# Maintained_by = ''.join(Reliance_Acks_Mitigation().Maintained_by)
# Maintained_by_backup = ','.join(Reliance_Acks_Mitigation().Maintained_by_backup)

# #print(Long_description)
# u.upload_doc_string_to_mysql(title, Path_, Parent_landing_page_path, Landing_page_path, Repository_path, Github_repository_path, Short_description, Long_description, Long_description_html, Technical_description, Databases_used, Technical_databases_used, Created_by, Maintained_by, Maintained_by_backup)
