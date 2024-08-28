import csv
import datetime

def log_now(
  function_name:str, 
  log_type:'error'or'warning'or'success', 
  message: str, 
  log_id: str
  ):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = [log_id, log_type, timestamp, function_name , message]

    with open("log.csv", "a", newline="") as log_file:
        writer = csv.writer(log_file)
        writer.writerow(log_entry)

# log_now("my_function", "error", "An error occurred")
