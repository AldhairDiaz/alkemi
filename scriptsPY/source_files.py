class Source_Files:
    
        
    def __init__(self):
        
        self.dir_default = 'filesCSV/'
        
    
    def get_datetime(self):
        from datetime import datetime  
                
        self.dt=datetime.now()
        self.dt_Y_M=self.dt.strftime('%Y')+'-'+self.dt.strftime('%B')
        self.dt_D_M_Y=self.dt.strftime('%d')+'-'+self.dt.strftime('%m')+'-'+self.dt.strftime('%Y')
        
        return self.dt_Y_M, self.dt_D_M_Y   
    
    
    def get_category_url(self,url):
        from posixpath import basename
        
        self.url=url
        self.path_url =  basename(self.url)
        self.format_name= self.path_url.replace('_','s ').split(' ')
        self.category=self.format_name[0].replace('.csv','s')
        
        return self.category
      
         
        
        
    def get_download_csv(self):
        import requests as req
        import os
       
        self.dt_YEAR_MOTH,self.dt_DAY_MONTH_YEAR=self.get_datetime()
        
        self.urls = [
            {
                'category':'biblioteca',
                'url':'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv'
            },
            {
                'category':'saladecine',
                'url':'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv'
            },
            {
                'category':'museo',
                'url':'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museo.csv'
            }
            
        ]
        
        
        for self.url in self.urls:            
            
            self.url_csv=self.url['url']
            
            self.category= self.get_category_url(self.url_csv)
            
            self.name_dir=f'{self.dir_default}{self.category}/{self.dt_YEAR_MOTH}/'
            self.file_csv_dir=f'{self.category}-{self.dt_DAY_MONTH_YEAR}.csv'
            
            
            if os.path.isfile(self.name_dir+self.file_csv_dir):
                print('ya existe el directorio y archivo...sobreescribiendo')
                
                self.url_requests=req.get(self.url_csv,allow_redirects=True)
                open(f'{self.name_dir}{self.file_csv_dir}','wb').write(self.url_requests.content)
                
            else:
                print('No existe...creando')
                
                os.makedirs(self.name_dir)
                self.url_requests=req.get(self.url_csv,allow_redirects=True)
                open(f'{self.name_dir}{self.file_csv_dir}','wb').write(self.url_requests.content)
            
            
            


name=Source_Files()
name.get_download_csv()