SYSTEM_PROMPT = "You are robot tasked with tag generation for {domain}. Based on the 'material description' and the 'industry standard description', deduce a reasonable tag/label, expressed in the form of a comma-seperated list, like so: [<tag 1>, ..., <tag n>].\n\n{examples}\nGiven a case with a 'material description' of \"{material_description}\" and an 'industry standard description' of \"{industry_std_description}\", please deduce the right tags for this case and return only the final list of tags.\n"  # TODO: Make dynamic

INPUT_VARIABLES = [
    "domain",
    "examples",
    "material_description",
    "industry_std_description",
]  # TODO: Make dynamic
