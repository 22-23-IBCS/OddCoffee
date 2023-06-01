from graphics import *
import math

username = input("Enter your Valorant username: ")
if username == "Makus":
    from Makus3683 import username, kills, deaths, wins, losses, assists, vandal_hs_pct, vandal_bs_pct, phantom_hs_pct, phantom_bs_pct, main_agent
elif username == "BurgerExpress":
    from BurgerExpress import username, kills, deaths, wins, losses, assists, vandal_hs_pct, vandal_bs_pct, phantom_hs_pct, phantom_bs_pct, main_agent
elif username == "Finnagann":
    from Finnagann import username, kills, deaths, wins, losses, assists, vandal_hs_pct, vandal_bs_pct, phantom_hs_pct, phantom_bs_pct, main_agent
elif username == "JohnDoe":
    from JohnDoe import username, kills, deaths, wins, losses, assists, vandal_hs_pct, vandal_bs_pct, phantom_hs_pct, phantom_bs_pct, main_agent


class ValorantStatsTracker:
    def __init__(self, username, kills, deaths, wins, losses, assists, vandal_hs_pct, vandal_bs_pct, phantom_hs_pct, phantom_bs_pct, main_agent):
        self.username = username
        self.kills = kills
        self.deaths = deaths
        self.wins = wins
        self.losses = losses
        self.assists = assists
        self.vandal_hs_pct = vandal_hs_pct
        self.vandal_bs_pct = vandal_bs_pct
        self.phantom_hs_pct = phantom_hs_pct
        self.phantom_bs_pct = phantom_bs_pct
        self.main_agent = main_agent

    def kill_death_ratio(self):
        if self.deaths == 0:
            return self.kills
        else:
            return self.kills / self.deaths

    def win_rate(self):
        total_matches = self.wins + self.losses
        if total_matches == 0:
            return 0.0
        else:
            return (self.wins / total_matches) * 100

    def better_assault_rifle(self):
        if self.vandal_hs_pct > self.phantom_hs_pct:
            return "Vandal"
        elif self.vandal_hs_pct < self.phantom_hs_pct:
            return "Phantom"
        else:
            if self.vandal_bs_pct > self.phantom_bs_pct:
                return "Vandal"
            elif self.vandal_bs_pct < self.phantom_bs_pct:
                return "Phantom"
            else:
                return "Both rifles are equally good."

    def recommended_youtuber(self):
        youtubers = {
            "Astra": "SoaR Maxie",
            "Breach": "Nosyy",
            "Brimstone": "zealfps",
            "Chamber": "TN6",
            "Cypher": "AcreTheDog",
            "Jett": "Tenz",
            "Kay/O": "Judgment",
            "Killjoy": "Keeoh",
            "Neon": "ShiroRz",
            "Omen": "Flexninja",
            "Phoenix": "Rawzu",
            "Raze": "Flights",
            "Reyna": "Noted",
            "Sage": "Grim",
            "Skye": "JimmyJam",
            "Sova": "AverageJonas",
            "Viper": "Raion",
            "Yoru": "Ziptie"
        }
        return youtubers.get(self.main_agent, "Unknown agent")

    def player_tier(self):
        win_rate = self.win_rate()
        k_d_ratio = self.kill_death_ratio()
        hs_percentage = self.vandal_hs_pct

        tiers = []

        if 50 < win_rate < 55:
            tiers.append("A tier")
        if 1.02 < k_d_ratio < 1.2:
            tiers.append("A tier")
        if 20 < hs_percentage < 35:
            tiers.append("A tier")
        if k_d_ratio > 1.2:
            tiers.append("S tier")
        if hs_percentage > 35:
            tiers.append("S tier")
        if win_rate > 55:
            tiers.append("S tier")
        if k_d_ratio < 1.2:
            tiers.append("C tier")
        if hs_percentage < 20:
            tiers.append("C tier")
        if win_rate < 50:
            tiers.append("C tier")

        if tiers:
            tier_counts = {tier: tiers.count(tier) for tier in tiers}
            max_count = max(tier_counts.values())
            overall_tier = [tier for tier, count in tier_counts.items() if count == max_count]
            return overall_tier[0]
        else:
            return "No tier assigned"


tracker = ValorantStatsTracker(username, kills, deaths, wins, losses, assists, vandal_hs_pct, vandal_bs_pct,
                               phantom_hs_pct, phantom_bs_pct, main_agent)

print("Kill Death Ratio:", tracker.kill_death_ratio())
print("Win Rate:", tracker.win_rate())
print("Better Assault Rifle:", tracker.better_assault_rifle())
print("Recommended YouTuber:", tracker.recommended_youtuber())
player_tier = tracker.player_tier()
print("Player Tier:", player_tier)

if player_tier == "S tier":
    win = GraphWin("Cyan Hexagon", 400, 400)
    win.setBackground("white")
    center_x, center_y = 200, 200
    side_length = 100
    angle = 2 * math.pi / 6
    vertices = []
    for i in range(6):
        x = center_x + side_length * math.cos(i * angle)
        y = center_y + side_length * math.sin(i * angle)
        vertices.append(Point(x, y))
    hexagon = Polygon(vertices)
    hexagon.setFill("cyan")
    hexagon.draw(win)
    

    text = Text(Point(center_x, center_y), 'S')
    text.setSize(20)
    text.setTextColor('black')
    text.setStyle('bold')
    text.draw(win)

elif player_tier == "A tier":
    win = GraphWin("Light Red Pentagon", 400, 400)
    win.setBackground("white")
    center_x, center_y = 200, 200
    side_length = 100
    angle = 2 * math.pi / 5
    start_angle = math.pi / 2  
    vertices = []
    for i in range(5):
        x = center_x + side_length * math.cos(start_angle + i * angle)
        y = center_y + side_length * math.sin(start_angle + i * angle)
        vertices.append(Point(x, y))
    pentagon = Polygon(vertices)
    pentagon.setFill("salmon")
    pentagon.draw(win)
    

    text = Text(Point(center_x, center_y), 'A')
    text.setSize(20)
    text.setTextColor('black')
    text.setStyle('bold')
    text.draw(win)

elif player_tier == "C tier":
    win = GraphWin("Light Green Square", 400, 400)
    win.setBackground("white")
    center_x, center_y = 200, 200
    side_length = 150
    square = Rectangle(Point(center_x - side_length / 2, center_y - side_length / 2),
                       Point(center_x + side_length / 2, center_y + side_length / 2))
    square.setFill("green")
    square.draw(win)
    

    text = Text(Point(center_x, center_y), 'C')
    text.setSize(20)
    text.setTextColor('black')
    text.setStyle('bold')
    text.draw(win)

win.getMouse()
win.close()

