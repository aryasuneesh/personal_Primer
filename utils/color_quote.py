import sys
root_dir='/home/fibel/personal_Primer'
sys.path.append(root_dir)

from Primer.Graphics.ColorQuoteDisplayer import ColorQuoteDisplayer

def main():
    # Define paths
    config_path = f'{root_dir}/primer.yaml'
    quotes_file_path = f'{root_dir}/assets/quotes.json'
    font_path = f"{root_dir}/assets/fonts/"
    output_image_path = 'quote_image.png'

    # Create an instance of ColorQuoteDisplayer
    displayer = ColorQuoteDisplayer(config_path, quotes_file_path)

    # Display a random quote
    displayer.display_random_quote()

if __name__ == '__main__':
    main()

