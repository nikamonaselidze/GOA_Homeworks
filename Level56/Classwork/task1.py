# Extract the domain name from a URL
def domain_name(url):
    
    url = url.split("//")[-1]
                            
    url = url.split("www.")[-1]
    
    last = url.split(".")[0]
    
    
    
    return last