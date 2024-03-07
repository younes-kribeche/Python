def time_to_text(heures, minutes):
    total_minutes = heures * 60 + minutes 
    heures = total_minutes // 60
    minutes_restantes = total_minutes % 60

    print(f"{heures} heures et {minutes_restantes} minutes")

time_to_text(5, 80)
    
    
