import pandas as pd 
from scraper import EPLScraper
from gsheet_utils import connect_to_google_sheet, upload_df_to_sheet

scraper = EPLScraper()

# Scrape final table
final_table_df = scraper.scrape_final_table()

# Derive and display Top Scorers
if final_table_df is not None:
    top_scorers_df = scraper.derive_top_scorers(final_table_df)
    print(top_scorers_df.head())

    # Derive and display Points per Game
    ppg_df = scraper.derive_ppg(final_table_df)
    print(ppg_df.head())

    # Derive and display Average Goals Scored per Match
    avg_goals_df = scraper.derive_avg_goals_per_match(final_table_df)
    print(avg_goals_df.head())



scraper = EPLScraper()
spreadsheet = connect_to_google_sheet("Premier League 2024/2025 Data")

# Scrape Final Table 
final_table_df = scraper.scrape_final_table()


if final_table_df is not None:
    # Upload Final Table
    upload_df_to_sheet(spreadsheet, "Final Table", final_table_df)
    

    # Upload Points per Game
    ppg_df = scraper.derive_ppg(final_table_df)
    upload_df_to_sheet(spreadsheet, "Points per Game", ppg_df)

    # Upload Avg Goals per Match
    avg_goals_df = scraper.derive_avg_goals_per_match(final_table_df)
    upload_df_to_sheet(spreadsheet, "Avg Goals Per Match", avg_goals_df)

     # Upload Top Scorers
    top_scorers_df = scraper.derive_top_scorers(final_table_df)
    upload_df_to_sheet(spreadsheet, "Top Scorers", top_scorers_df)

#  Scrape Squad Goalkeeping Table
squad_goalkeeping_df = scraper.scrape_squad_goalkeeping()

if squad_goalkeeping_df is not None:
    # Remove any unnamed multi-index or extra headers
    if isinstance(squad_goalkeeping_df.columns, pd.MultiIndex):
        squad_goalkeeping_df.columns = squad_goalkeeping_df.columns.get_level_values(-1)
    
    squad_goalkeeping_df.columns = [col if 'Unnamed' not in str(col) else '' for col in squad_goalkeeping_df.columns]

    # Upload Squad Goalkeeping Table
    upload_df_to_sheet(spreadsheet, "Squad Goalkeeping", squad_goalkeeping_df)