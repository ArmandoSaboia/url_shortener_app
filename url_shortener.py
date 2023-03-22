import streamlit as st
import pyshorteners

def main():
	st.title('URL Shortener')
	st.markdown('## Simplify your URLs, links & manage them')

	# Create a text input field for the user to enter the long URL
	url = st.text_input("Enter the URL to shorten")

	# Create a button for the user to submit the long URL and get the shortened URL
	if st.button("Shorten"):
     	# Use pyshorteners library to generate the shortened URL
    		s = pyshorteners.Shortener()
    		shortened_url = s.tinyurl.short(url)
       	# Display the shortened URL to the user
    		st.success("Shortened URL: {}".format(shortened_url))
    
if __name__ == '__main__':
    main()
