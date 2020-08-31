# Error_log_webpage
It is a project created on python which first reads the log file and then create a csv file based on user and based on error log. Then it converts tht csv's to html for web view.

# To run this project
First we have to create a folder and take all 3 files in the folder.

Then from command line we can execute "create_csv.py" as
home@Sar***:~/new_folder$ ./create_csv.py
 # after Running the create_csv.py It will create two files-
 error_message.csv and user_statistics.csv
 
 Then we have to perform two commands sequentially
 home@Sar***:~/new_folder$ ./csv_to_html.py error_message.csv /www/html error_message.html
 
 then this one
 home@Sar***:~/new_folder$ ./csv_to_html.py user_statistics.csv /www/html user_statistics.html
 
 in the above two commands first we have to give executable name then the csv file then the destination folder then destination filename.
 
 After this two html file will be created.
