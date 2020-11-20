__author__ = "Thomas McGinn"
__credits__ = ["Thomas McGinn"]
__maintainer__ = "Thomas McGinn"


from search import Search
import utilities as u

class Zero_Forty_Five_Categorization_Extract(Search):
    def __init__(self):
        super().__init__()
        self.title = 				[
                                    'all_categories',
                                    'sensor_expiration',
                                    'g5_g6_app_no_alert',
                                    'g5_g6_app_no_audio_vibration',
                                    'no_alert_audio_vibration_app',
                                    'alert_issue',
                                    'watch_issue',
                                    # 'forced_manual_calibrations',
                                    'android_excessive_alert',
                                    'follow_app_issue',
                                    'clarity_issue',
                                    'calibration_issue',
                                    'display_issue_app',
                                    'bent_sensor_stuff',
                                    'erratic_egv_readings',
                                    'excessive_alert',
                                    'sensor_code_issue',
                                    'warm_up_restarted',
                                    'premature_countdown',
                                    'start_new_sensor',
                                    'app_issue',
                                    'interaction_issue',
                                    'not_evaluated',
                                    ]
        self.Path_ = [r'Z:\QA\Customer Returns-Complaint System\Thomas-Jesse\Searches']
        self.Parent_landing_page_path = ['#']
        self.Landing_page_path = [r'#']
        self.Repository_path = [r'C:\Users\[username]\Desktop\Customer-Advocacy-Searches\Library\Complaints/zero_forty_five_categorization.py']
        self.Github_repository_path = [r'https://github.com/dexcom-inc/Customer-Advocacy-Searches/blob/master/Library/Complaints/zero_forty_five_categorization.py']
        self.Short_description = ['045 complaints for a specific category or given categories']
        self.Long_description = ['#']                                    
        self.Long_description_html = ['These searches display all 045 complaints for a given category or categories. These excel files contain the following sheets:'
                            +'<ul style="list-style-type:circle;font-size:14px">'
                            + '<li>Report:'
                            +   '<ul style="list-style-type:square;font-size:12px">'
                            +     '<li>All 045 complaints for a specific category or given categories</li>'
                            +   '</ul>'
                            + '</li>'
                            + '<li>Overview:'
                            +   '<ul style="list-style-type:square;font-size:12px">'
                            +       '<li>Summary by Category and Sub-Category</li>'
                            +   '</ul>'
                            + '</li>'
                            + '<li>Event Type:'
                            +   '<ul style="list-style-type:square;font-size:12px">'
                            +       '<li>Summary by Event Type and Category</li>'
                            +   '</ul>'
                            + '</li>'
                            + '<li>By Alert Date:'
                            +   '<ul style="list-style-type:square;font-size:12px">'
                            +       '<li>Summary by Category and Alert Date</li>'
                            +   '</ul>'
                            + '</li>'
                            + '<li>By Device Type:'
                            +   '<ul style="list-style-type:square;font-size:12px">'
                            +       '<li>Summary by Device Type, Category, and Sub-Category</li>'
                            +   '</ul>'
                            + '</li>'
                            + '<li>By Alert and Device:'
                            +   '<ul style="list-style-type:square;font-size:12px">'
                            +       '<li>Summary by Device Type, Category, Sub-Category, and Alert Date</li>'
                            +   '</ul>'
                            + '</li>'
                            +'</ul>']
        self.Technical_description = ["#"]
        self.Databases_used = ['customer_advocacy_reliance','customer_advocacy_agile','customer_advocacy_pms']
        self.Technical_databases_used = ['customer_advocacy_reliance','reliance-prod']
        self.Created_by = [__author__]
        self.Maintained_by = [__maintainer__]
        self.Maintained_by_backup = ['#']      

# for t in Zero_Forty_Five_Categorization_Extract().title:
#     title = t
#     Path_ = ''.join(Zero_Forty_Five_Categorization_Extract().Path_)
#     Path_ = Path_.replace('\\', '\\\\')
#     Parent_landing_page_path = ''.join(Zero_Forty_Five_Categorization_Extract().Parent_landing_page_path)
#     Parent_landing_page_path = Parent_landing_page_path.replace('\\', '\\\\')
#     Landing_page_path = ''.join(Zero_Forty_Five_Categorization_Extract().Landing_page_path)
#     Landing_page_path = Landing_page_path.replace('\\', '\\\\')
#     Landing_page_path = Landing_page_path.replace('%20', ' ')
#     Repository_path = ''.join(Zero_Forty_Five_Categorization_Extract().Repository_path)
#     Repository_path = Repository_path.replace('\\', '\\\\')
#     Github_repository_path = ''.join(Zero_Forty_Five_Categorization_Extract().Github_repository_path)
#     Short_description = ''.join(Zero_Forty_Five_Categorization_Extract().Short_description)
#     Long_description = ''.join(Zero_Forty_Five_Categorization_Extract().Long_description)
#     Long_description = Long_description.replace("'", "\\'")
#     Long_description_html = ''.join(Zero_Forty_Five_Categorization_Extract().Long_description_html)
#     Long_description_html = Long_description_html.replace('\\', '\\\\')
#     Long_description_html = Long_description_html.replace("'", "\\'")
#     Long_description_html = Long_description_html.replace('"', '\\"')
#     Technical_description = ''.join(Zero_Forty_Five_Categorization_Extract().Technical_description)
#     Technical_description = Technical_description.replace("'", "\\'")
#     Databases_used = ','.join(Zero_Forty_Five_Categorization_Extract().Databases_used)
#     Technical_databases_used = ','.join(Zero_Forty_Five_Categorization_Extract().Technical_databases_used)
#     Created_by = ''.join(Zero_Forty_Five_Categorization_Extract().Created_by)
#     Maintained_by = ''.join(Zero_Forty_Five_Categorization_Extract().Maintained_by)
#     Maintained_by_backup = ','.join(Zero_Forty_Five_Categorization_Extract().Maintained_by_backup)

#     u.upload_doc_string_to_mysql(title, Path_, Parent_landing_page_path, Landing_page_path, Repository_path, Github_repository_path, Short_description, Long_description, Long_description_html, Technical_description, Databases_used, Technical_databases_used, Created_by, Maintained_by, Maintained_by_backup)
