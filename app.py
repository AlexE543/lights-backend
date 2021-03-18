from apis import create_app
from utils.light_strand import LightStrand

app, api = create_app()

global light_strand
light_strand = LightStrand(144, brightness=0.2)

if __name__ == '__main__':
   app.run(debug=True, port=80, host='0.0.0.0')
