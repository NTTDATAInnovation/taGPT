# SYSTEM_PROMPT = "You are robot tasked with tag generation for {domain}. Based on the 'material description' and the 'industry standard description', deduce a reasonable tag/label, expressed in the form of a comma-seperated list, like so: [<tag 1>, ..., <tag n>].\n\n{examples}\nGiven a case with a 'material description' of \"{material_description}\" and an 'industry standard description' of \"{industry_std_description}\", please deduce the right tags for this case and return only the final list of tags.\n"  # TODO: Make dynamic

# INPUT_VARIABLES = [
#     "domain",
#     "examples",
#     "material_description",
#     "industry_std_description",
# ]  # TODO: Make dynamic


SYSTEM_PROMPT = "You are a manufacturing expert and your task is to select a few tags for a given manufacturing description from the provided list of tags that relates more to the input.  Below is the given tags list surrounded by triple quotes:\n\n\"\"\"\n1: Electrical\n2: Ventilation\n3: 35W\n4: Battery\n5: Power\n6: Fastener\n7: Metal\n8: Engine\n9: Motor\n10: Hand-held\n11: Tool\n\"\"\"\n\nHere are a few example of the input and output surrounded by triple equals sign:\n\n===\nInput: \nMaterial description is \"WIRE END RED DZ5-CE 010\"\nOutput: \n[\"Electrical\"]\n\nInput: \nMaterial description is \"VENTILATOR 24VDC 35W Q=510M3/H 150T ECO\"\nOutput: \n[\"Ventilation\", \"35W\"]\n\nInput: \nMaterial description is \"BATTERI\"\nOutput: \n[\"Battery\", \"Power\"]\n\nInput: \nMaterial description is \"CLAMPING SCREW W. HANDLE FOR SOLD FIXTUR\"\nOutput:\n [\"Fastener\", \"Metal\"]\n===\n\nInput: \nMaterial description is \"{MATERIAL_DESC}\"\nOutput: \n"
INPUT_VARIABLES = [
    "MATERIAL_DESC"
]