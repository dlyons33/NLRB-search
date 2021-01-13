
NEXT
    > A lot of the code I added to base.html needs to be moved to home.html
    > Finish styling main splash page (top div)
        > Center text
        > Add arrow/text re: scrolling / summary at bottom right of page
    > Do something with Contact form
    > Finish footer

DATABSE
    > Scrape PDFs by going through links saved in csv
    > Parse PDFs into text blobs for use in searches
    > Create Postgres instance in Docker
    > Create/load database with scraped data
    > Connect Django to Postgres DB 

WEB API
    > Handles searches & results
    > Handles saving decisions
    > Handles logging decisions
    > Manages list of saved decisions & search history
    > API for entering in backlog of weekly summaries programatically

STYLE
    > Flash messages for successful/unsuccessful login, logout & registration
    > Flash message for submitting contact form
    > Why are nav bar links disappearing on smaller view sizes?
    > Turn nav bar items into a drop down menu for small view sizes?
    > Sticky header at top and footer at bottom

User / Profile
    > Profile page
        - User info
        - Recent searches
        - Saved decisions
    > Add email to user profile
    > Reset password via email

POSSIBLE EXTRAS

Add to top nav bar in {if} loop if user is_authenticated:
    > Saved decisions
    > Recent searches
    > Make bootstrap drop down menu?
    > To be populated dynamically by React call on page load?
    > Last element is link for more than N recent