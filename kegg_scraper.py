import urllib.request
from bs4 import BeautifulSoup
import ssl
import requests
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

list_links = []

# Open the file safely
with open("C:\\Users\\sd01165\\Desktop\\metabolic_model\\visualization\\ghostkola_res2.txt") as gene_id:
    for id in gene_id:
        id = id.strip()  # Remove whitespace or newline characters
        print(id)

        # Construct the URL
        url = (
            f'https://www.kegg.jp/kegg-bin/blastkoala_result_gene_list'
            f'?id=8ef6735f332d64cc31429738c04131df05e7a987&passwd=0HTOdi&type=ghostkoala&code=user&target={id}'
        )
        
        try:
            html = urllib.request.urlopen(url, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')

            # Retrieve all anchor tags
            tags = soup('a')
            for tag in tags:
                sec_link = tag.get('href', None)
                if sec_link:
                    list_links.append(sec_link)

            if not list_links:
                print("No links found for this ID.")
                continue

            print(list_links[0])

            # Process the first link
            url2 = 'https://www.kegg.jp' + list_links[0]
            print(url2)

            # Fetch the second URL
            html2 = requests.get(url2)
            html_content = html2.text
            soup2 = BeautifulSoup(html_content, 'html.parser')

            # Match WBGene pattern
            ens_pattern = re.compile(r'WBGene\d+')
            found = soup2.find(text=ens_pattern)
            print(found)

            # Find NCBI gene links
            ncbi = soup2.select('a[href*=ncbi.nlm.nih.gov/gene]')
            if ncbi:
                print([link['href'] for link in ncbi if 'href' in link.attrs])
            else:
                print("No NCBI gene links found.")

        except Exception as e:
            print(f"An error occurred: {e}")
