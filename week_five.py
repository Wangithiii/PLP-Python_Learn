class FormulaOneTeam:
    def __init__(self, name, headquarters, team_principal, championships_won):
        self.name= name
        self.headquarters= headquarters
        self.team_principal= team_principal
        self.championships_won= championships_won

    def team_info(self):
        return(f"Team: {self.name}/n"
               f"Headquarters: {self.headquarters}/n"
               f"Team Principal:{self.team_principal}/n"
               f"Championships Won: {self.championships_won}/n")
    
    def win_championship(self):
        self.championships_won +=1
        print(f"Congratulations! {self.name} has now won {self.championships_won} championships!")

#Inherited class
class Ferrari(FormulaOneTeam):
    def __init__(self, driver_1, driver_2, car_model):
        super().__init__("Ferrari","Maranello, Italy", "Fred Vasseur", 16)
        self.driver_1= driver_1
        self.driver_2= driver_2
        self.car_model= car_model
    
    def car_info(self):
        return(f"Ferrari Car Model: {self.car_model}/n"
               f"Drivers: {self.driver_1} and {self.driver_2}")
    
    def race_win(self, race_name):
        print(f"Ferrari wins the {race_name}! A brilliant performance by {self.driver_1} and {self.driver_2}!")

ferrari_team= Ferrari (driver_1="Charles Leclerc", driver_2="Carlos Sainz"m car_model="SF=24")
print(ferrari_team.team_info())
print(ferrari_team.car_info())
ferrari_team.win_championship()
ferrari_team.race_win("Monaco Grand Prix")