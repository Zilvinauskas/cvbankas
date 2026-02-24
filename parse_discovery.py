from parsel import Selector
import csv

def main():
    
    title = 0 
    links = []  

    while True:       
        
        try:
            # open html
            with open(f"html/file{title}.html", "r") as file:
                print(f"Opening file no:{title}")            
                html = file.read()
            
            # select data
            selector = Selector(text=html)
            job_cards = selector.css("a.list_a")
            
            # append links to list
            for card in job_cards:
                links.append(card.css("::attr(href)").get())                            
            
            title += 1
        
        #catch exception with last html file
        except FileNotFoundError:
            print("done")
            break
        
    # create txt and paste all links from list
    with open(f"links.txt", "w") as file:
        for link in links:            
            file.write(link.strip() + "\n")
        
if __name__ == "__main__":
    main()