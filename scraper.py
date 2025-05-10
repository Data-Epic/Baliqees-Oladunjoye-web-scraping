from utils import read_html_file
import pandas as pd
from io import StringIO
import gspread


class EPLScraper:
    def __init__(self):
        print("Initializing EPL Scraper...")
        self.soup = read_html_file()

    def scrape_final_table(self):
        print("Scraping Final Table...")
        table = self.soup.find('table', {'id': 'results2024-202591_overall'})
        if table is None:
            print("Final Table not found.")
            return None
        df = pd.read_html(StringIO(str(table)))[0]
        df.dropna(axis=1, how='all', inplace=True)
        if 'Notes' in df.columns:
            df.drop(columns=['Notes'], inplace=True)
        return df

    def scrape_squad_goalkeeping(self):
        print("Scraping Squad Goalkeeping Table...")
        table = self.soup.find('table', {'id': 'stats_squads_keeper_for'})
        if table is None:
            print("Squad Goalkeeping Table not found.")
            return None
        df = pd.read_html(StringIO(str(table)))[0]
        df.dropna(axis=1, how='all', inplace=True)
        return df

    def derive_top_scorers(self, final_table_df):
        print("Deriving Top Scorers...")
        scorers_df = final_table_df[['Squad', 'Top Team Scorer']].dropna()

        clean_scorers = []
        for _, row in scorers_df.iterrows():
            squad = row['Squad']
            scorer_info = row['Top Team Scorer']
            if ' - ' in scorer_info:
                names_part, goals_part = scorer_info.rsplit(' - ', 1)
                goals = int(goals_part)
                players = [name.strip() for name in names_part.split(',')]
                for player in players:
                    clean_scorers.append({'Squad': squad, 'Player': player, 'Goals': goals})

        top_scorers_df = pd.DataFrame(clean_scorers)
        return top_scorers_df.sort_values(by='Goals', ascending=False).reset_index(drop=True)

    def derive_ppg(self, final_table_df):
        print("Calculating Points per Game (PPG)...")
        final_table_df['PPG'] = (final_table_df['Pts'] / final_table_df['MP']).round(2)
        ppg_df = final_table_df[['Squad', 'MP', 'Pts', 'PPG']].sort_values(by='PPG', ascending=False).reset_index(drop=True)
        return ppg_df

    def derive_avg_goals_per_match(self, final_table_df):
        print("Calculating Average Goals Scored per Match...")
        final_table_df['Avg_Goals_For'] = (final_table_df['GF'] / final_table_df['MP']).round(2)
        avg_goals_df = final_table_df[['Squad', 'MP', 'GF', 'Avg_Goals_For']].sort_values(by='Avg_Goals_For', ascending=False).reset_index(drop=True)
        return avg_goals_df


    def upload_df_to_sheet(self, spreadsheet, worksheet_name, df):
        """Uploads a DataFrame to a Google Sheets worksheet."""
        df = self.flatten_columns(df)

        try:
            worksheet = spreadsheet.worksheet(worksheet_name)
        except gspread.exceptions.WorksheetNotFound:
            worksheet = spreadsheet.add_worksheet(title=worksheet_name, rows="1000", cols="30")

        worksheet.clear()

    def flatten_columns(self, df):
    #Flattens multi-index columns if present
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = [' '.join(col).strip() for col in df.columns.values]
        return df

        # Insert headers
        worksheet.insert_row(df.columns.tolist(), 1)

        # Insert data rows
        worksheet.insert_rows(df.values.tolist(), 2)

        print(f"Uploaded to '{worksheet_name}' successfully!")