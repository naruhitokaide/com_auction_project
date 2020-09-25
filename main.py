from auction import create_app

if __name__ == "__main__":
    napp=create_app()
    napp.secret_key='iab207assesment3'
    napp.run(debug=True)