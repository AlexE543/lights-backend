from apis import create_app
from utils.light_strand import LightStrand

app, api = create_app()

global light_strand
light_strand = LightStrand(144, brightness=0.2)
