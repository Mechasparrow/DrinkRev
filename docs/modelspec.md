# Model Spec 

## Drink
- pk
- name (CharField)
- desc (TextField)
- img_url (URLField)

## DrinkReview
- pk
- fk (-> Drink)
- rating (Int)
