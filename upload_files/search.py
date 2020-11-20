import utilities as u

class Search(object):
    test_con = u.get_test_connection()
    def __init__(self, title=['No Title Provided'], description=['No Description Provided']):
        self._df_ = None
        self._df_historical = None
        self._databases_needed = None
        self.title = title
        self.description = description
    
    def transform_columns(self):
        for t in self.title:
            title = t
            Path_ = ''.join(self.Path_)
            Path_ = Path_.replace('\\', '\\\\')
            Parent_landing_page_path = ''.join(self.Parent_landing_page_path)
            Parent_landing_page_path = Parent_landing_page_path.replace('\\', '\\\\')
            Landing_page_path = ''.join(self.Landing_page_path)
            Landing_page_path = Landing_page_path.replace('\\', '\\\\')
            Landing_page_path = Landing_page_path.replace('%20', ' ')
            Repository_path = ''.join(self.Repository_path)
            Repository_path = Repository_path.replace('\\', '\\\\')
            Github_repository_path = ''.join(self.Github_repository_path)
            Short_description = ''.join(self.Short_description)
            Long_description = ''.join(self.Long_description)
            Long_description = Long_description.replace("'", "\\'")
            Long_description_html = ''.join(self.Long_description_html)
            Long_description_html = Long_description_html.replace('\\', '\\\\')
            Long_description_html = Long_description_html.replace("'", "\\'")
            Long_description_html = Long_description_html.replace('"', '\\"')
            Technical_description = ''.join(self.Technical_description)
            Technical_description = Technical_description.replace("'", "\\'")
            Databases_used = ','.join(self.Databases_used)
            Technical_databases_used = ','.join(self.Technical_databases_used)
            Created_by = ''.join(self.Created_by)
            Maintained_by = ''.join(self.Maintained_by)
            Maintained_by_backup = ','.join(self.Maintained_by_backup)

            u.upload_doc_string_to_mysql(title, Path_, Parent_landing_page_path, Landing_page_path, Repository_path, Github_repository_path, Short_description, Long_description, Long_description_html, Technical_description, Databases_used, Technical_databases_used, Created_by, Maintained_by, Maintained_by_backup)




