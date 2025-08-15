import requests
import sys
import json
import os
from typing import Dict, Any

# API credentials
API_URL = "https://pakdatabase.site/api/search.php"
API_USERNAME = "Kami"
API_PASSWORD = "123456"

# ANSI color codes for beautiful output
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    # Regular colors
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright colors
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

def clear_screen():
    """Clear the terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')

def print_logo():
    """Print the custom TABBU logo"""
    logo = f"""
{Colors.BRIGHT_GREEN}┏┳┓┏┓┳┓┳┓┳┳  ┏┓ ┳ ┳┳┓  ┳┓┏┓┏┳┓┏┓
{Colors.BRIGHT_WHITE} ┃ ┣┫┣┫┣┫┃┃  ┗┓ ┃ ┃┃┃  ┃┃┣┫ ┃ ┣┫
{Colors.BRIGHT_GREEN} ┻ ┛┗┻┛┻┛┗┛  ┗┛ ┻ ┛ ┗  ┻┛┛┗ ┻ ┛┗{Colors.BRIGHT_GREEN}
{Colors.BRIGHT_WHITE}──────────────────────────────────────────────────
{Colors.BRIGHT_YELLOW} DEVELOPER: {Colors.BRIGHT_BLUE} TABBU ARAIN
{Colors.BRIGHT_YELLOW} TOOLS:     {Colors.CYAN} SIM {Colors.BRIGHT_RED}DETAILS
{Colors.BRIGHT_YELLOW} STATUS:    {Colors.BRIGHT_YELLOW} {Colors.BRIGHT_GREEN}FREE
{Colors.BRIGHT_WHITE}──────────────────────────────────────────────────{Colors.RESET}"""
    print(logo)

def print_separator():
    """Print a professional separator line"""
    print(f"{Colors.BRIGHT_CYAN}{'═' * 80}{Colors.RESET}")

def print_search_status(search_term: str):
    """Print professional search status"""
    print(f"\n{Colors.BG_YELLOW}{Colors.BRIGHT_WHITE} INITIATING SEARCH PROTOCOL {Colors.RESET}")
    print(f"{Colors.BRIGHT_YELLOW}╭─────────────────────────────────────────────────╮{Colors.RESET}")
    print(f"{Colors.BRIGHT_YELLOW}│{Colors.RESET} {Colors.BRIGHT_WHITE}Target: {Colors.RESET} {Colors.BRIGHT_CYAN}{search_term}{Colors.RESET}")
    print(f"{Colors.BRIGHT_YELLOW}│{Colors.RESET} {Colors.BRIGHT_WHITE}Status:{Colors.RESET} {Colors.BRIGHT_GREEN} Connected To Database.{Colors.RESET}")
    print(f"{Colors.BRIGHT_YELLOW}│{Colors.RESET} {Colors.BRIGHT_WHITE}Version:{Colors.RESET} {Colors.BRIGHT_MAGENTA}1.0{Colors.RESET}")
    print(f"{Colors.BRIGHT_YELLOW}╰─────────────────────────────────────────────────╯{Colors.RESET}")

def search_sim_data(search_term: str) -> Dict[str, Any]:
    """Search for SIM data using the external API."""
    try:
        print_search_status(search_term)
        
        params = {
            'username': API_USERNAME,
            'password': API_PASSWORD,
            'search_term': search_term
        }
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        print(f"{Colors.BRIGHT_GREEN}✅ Data retrieval successfull{Colors.RESET}")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"\n{Colors.BG_RED}{Colors.BRIGHT_WHITE} ❌ CONNECTION ERROR {Colors.RESET}")
        print(f"{Colors.BRIGHT_RED}╭─────────────────────────────────────────╮{Colors.RESET}")
        print(f"{Colors.BRIGHT_RED}│{Colors.RESET} {Colors.BRIGHT_WHITE}Error Details:{Colors.RESET} {str(e)[:30]}...")
        print(f"{Colors.BRIGHT_RED}╰─────────────────────────────────────────╯{Colors.RESET}")
        return {}

def format_field_name(field_name: str) -> str:
    """Format field names with appropriate icons"""
    field_icons = {
        'name': '👤',
        'phone': '📱',
        'number': '📱',
        'address': '🏠',
        'cnic': '🆔',
        'city': '🏙️',
        'operator': '📡',
        'network': '🌐'
    }
    
    clean_name = field_name.lower().replace('_', ' ').strip()
    icon = field_icons.get(clean_name, '📋')
    formatted_name = field_name.replace('_', ' ').title()
    
    return f"{icon} {formatted_name}"

def should_display_field(field_name: str) -> bool:
    """Check if field should be displayed"""
    excluded_fields = {
        'id', 'imsi', 'data_sim', 'data sim', 'passport', 
        'company', 'phone_res', 'phone res', 'phone_off', 'phone off'
    }
    
    clean_name = field_name.lower().replace('_', ' ').replace('-', ' ').strip()
    return clean_name not in excluded_fields

def display_results(data: Dict[str, Any]) -> None:
    """Display the search results in a professional format"""
    if not data:
        print(f"\n{Colors.BG_RED}{Colors.BRIGHT_WHITE} ❌ SEARCH RESULT: NO DATA FOUND {Colors.RESET}")
        print(f"{Colors.BRIGHT_RED}╭─────────────────────────────────────────────────────╮{Colors.RESET}")
        print(f"{Colors.BRIGHT_RED}│{Colors.RESET} {Colors.YELLOW}💡 Troubleshooting:{Colors.RESET}                                {Colors.BRIGHT_RED}{Colors.RESET}")
        print(f"{Colors.BRIGHT_RED}│{Colors.RESET}   • Verify number format (03XXXXXXXXX)              {Colors.BRIGHT_RED}{Colors.RESET}")
        print(f"{Colors.BRIGHT_RED}│{Colors.RESET}   • Check internet connection                        {Colors.BRIGHT_RED}{Colors.RESET}")
        print(f"{Colors.BRIGHT_RED}│{Colors.RESET}   • Try different number format                      {Colors.BRIGHT_RED}{Colors.RESET}")
        print(f"{Colors.BRIGHT_RED}╰─────────────────────────────────────────────────────╯{Colors.RESET}")
        return
    
    found_data = False
    all_numbers = set()
    total_records = 0
    
    print(f"\n{Colors.BG_GREEN}{Colors.BRIGHT_WHITE} SEARCHED SIM DATA REPORT {Colors.RESET}")
    print(f"{Colors.BRIGHT_GREEN}{'═' * 76}{Colors.RESET}")
    
    for network in data:
        records = data[network]
        if isinstance(records, list) and records:
            found_data = True
            network_count = len(records)
            total_records += network_count
            
            # Professional network header
            print(f"{Colors.BRIGHT_GREEN}{Colors.RESET} {Colors.BG_BLUE}{Colors.BRIGHT_WHITE} 📡 {network.upper()} TELECOMMUNICATION NETWORK {Colors.RESET} {Colors.BRIGHT_BLUE}({network_count} records){Colors.RESET} {Colors.BRIGHT_GREEN}{Colors.RESET}")
            print(f"{Colors.BRIGHT_GREEN}{'─' * 76}{Colors.RESET}")
            
            for i, record in enumerate(records, 1):
                if isinstance(record, dict):
                    # Record header with professional styling
                    print(f"{Colors.BRIGHT_GREEN}{Colors.RESET} {Colors.BG_CYAN}{Colors.BRIGHT_WHITE} RECORD #{i:02d} {Colors.RESET}")
                    print(f"{Colors.BRIGHT_GREEN}{Colors.RESET} {Colors.BRIGHT_CYAN}─────────────────────────────────────────────────────────────────────────{Colors.RESET}")
                    
                    # Group fields by importance
                    primary_fields = []
                    secondary_fields = []
                    
                    for key, value in record.items():
                        if value and str(value).strip() and should_display_field(key):
                            if key.lower() in ['name', 'number', 'cnic']:
                                primary_fields.append((key, value))
                            else:
                                secondary_fields.append((key, value))
                            
                            if key.lower() == 'number' and value:
                                all_numbers.add(str(value))
                    
                    # Display primary fields first
                    for key, value in primary_fields:
                        formatted_field = format_field_name(key)
                        print(f"{Colors.BRIGHT_GREEN}│{Colors.RESET} {Colors.BRIGHT_CYAN}{Colors.RESET} {Colors.BRIGHT_WHITE}{formatted_field:<28}{Colors.RESET} {Colors.BRIGHT_GREEN}▶{Colors.RESET} {Colors.BRIGHT_YELLOW}{value}{Colors.RESET}")
                    
                    if primary_fields and secondary_fields:
                        print(f"{Colors.BRIGHT_GREEN}│{Colors.RESET} {Colors.BRIGHT_CYAN}─────────────────────────────────────────────────────────────────────────{Colors.RESET}")
                    
                    # Display secondary fields
                    for key, value in secondary_fields:
                        formatted_field = format_field_name(key)
                        print(f"{Colors.BRIGHT_GREEN}│{Colors.RESET} {Colors.BRIGHT_CYAN}{Colors.RESET} {Colors.WHITE}{formatted_field:<28}{Colors.RESET} {Colors.GREEN}▶{Colors.RESET} {Colors.CYAN}{value}{Colors.RESET}")
                    
                    print(f"{Colors.BRIGHT_GREEN}{Colors.RESET} {Colors.BRIGHT_CYAN}─────────────────────────────────────────────────────────────────────────{Colors.RESET}")
                    
                    if i < len(records):
                        print(f"{Colors.BRIGHT_GREEN}{Colors.RESET}")
            
            print(f"{Colors.BRIGHT_GREEN}{'═' * 76}{Colors.RESET}")
    
    if not found_data:
        print(f"{Colors.BRIGHT_GREEN}{Colors.RESET} {Colors.BRIGHT_RED}❌ NO RECORDS FOUND{Colors.RESET}")
        print(f"{Colors.BRIGHT_GREEN}{'═' * 76}╯{Colors.RESET}")
        
        if all_numbers:
            print(f"{Colors.BRIGHT_GREEN}{Colors.RESET} {Colors.BRIGHT_WHITE}📱 Unique Numbers:{Colors.RESET} {Colors.BRIGHT_YELLOW}{len(all_numbers)}{Colors.RESET}")
            print(f"{Colors.BRIGHT_GREEN}{Colors.RESET}")
            for number in sorted(all_numbers):
                print(f"{Colors.BRIGHT_GREEN}{Colors.RESET}   {Colors.BRIGHT_GREEN}▶{Colors.RESET} {Colors.BRIGHT_CYAN}{number}{Colors.RESET}")
        
        print(f"{Colors.BRIGHT_GREEN}{'═' * 76}{Colors.RESET}")

def get_user_input() -> str:
    """Get user input with professional prompt"""
    try:
        user_input = input(f"{Colors.BRIGHT_WHITE}🔍 ENTER TARGET NUMBER:{Colors.RESET} {Colors.BRIGHT_GREEN}▶{Colors.RESET} ").strip()
        return user_input
    except KeyboardInterrupt:
        print(f"\n{Colors.BRIGHT_RED}👋 Session terminated. Thank you for using TABBU Sim Details Tool!{Colors.RESET}")
        sys.exit(0)

def validate_input(search_term: str) -> bool:
    """Validate the input"""
    if not search_term:
        print(f"{Colors.BRIGHT_RED}❌ Please enter a valid number!{Colors.RESET}")
        return False
    
    if search_term.lower() == 'exit':
        print(f"{Colors.BRIGHT_GREEN}👋 Thank you for using TABBU Sim Details Tool! Goodbye!{Colors.RESET}")
        sys.exit(0)
    
    # Clean the search term
    cleaned = search_term.replace('-', '').replace(' ', '').replace('+92', '0')
    
    if len(cleaned) < 10:
        print(f"{Colors.BRIGHT_RED}❌ Number too short! Please enter a valid Pakistani number.{Colors.RESET}")
        return False
    
    return True

def main():
    """Main function"""
    try:
        while True:
            clear_screen()
            print_logo()
            
            search_term = get_user_input()
            
            if not validate_input(search_term):
                input(f"\n{Colors.BRIGHT_YELLOW}Press Enter to continue...{Colors.RESET}")
                continue
            
            # Clean the search term
            clean_term = search_term.replace('-', '').replace(' ', '').replace('+92', '0')
            
            print_separator()
            data = search_sim_data(clean_term)
            display_results(data)
            
            print(f"\n{Colors.BG_MAGENTA}{Colors.BRIGHT_WHITE} IF YOU WANT TO CONTINUE SESSION {Colors.RESET}")
            print(f"{Colors.BRIGHT_MAGENTA}╭──────────────────────────────────────────────╮{Colors.RESET}")
            print(f"{Colors.BRIGHT_MAGENTA}│{Colors.RESET} {Colors.BRIGHT_GREEN}Press [ENTER] to{Colors.RESET} Continue searching              {Colors.BRIGHT_MAGENTA}{Colors.RESET}")
            print(f"{Colors.BRIGHT_MAGENTA}│{Colors.RESET} {Colors.BRIGHT_RED}Perss [N] to{Colors.RESET} Exit application                   {Colors.BRIGHT_MAGENTA}{Colors.RESET}")
            print(f"{Colors.BRIGHT_MAGENTA}╰──────────────────────────────────────────────╯{Colors.RESET}")
            
            choice = input(f"{Colors.BG_YELLOW}ENTER or N ?{Colors.RESET} {Colors.BRIGHT_MAGENTA}▶{Colors.RESET} ").strip().lower()
            
            if choice == 'n' or choice == 'no':
                print(f"\n{Colors.BG_GREEN}{Colors.BRIGHT_WHITE} ✅ SESSION TERMINATED {Colors.RESET}")
                print(f"{Colors.BRIGHT_GREEN}Thank you for using TABBU sim Details Tool!{Colors.RESET}")
                break
    
    except KeyboardInterrupt:
        print(f"\n{Colors.BRIGHT_RED}👋 Goodbye!{Colors.RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"{Colors.BRIGHT_RED}❌ Unexpected error: {str(e)}{Colors.RESET}")
        sys.exit(1)

if __name__ == '__main__':
    main()
