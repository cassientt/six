# unprinted_designs = ['phone case', 'robot pendant', 'document']
#
# completed_models = []
#
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f'Printing {current_design.title()}: ')
#     completed_models.append(current_design)
# print(f'The following models have been printed:')
# for completed_model in completed_models:
#     print(completed_model.title())


def print_models(unprinted_design, completed_model):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing {current_design.title()}: ')
        completed_models.append(current_design)


def show_completed_models(completed_model):
    print(f'The following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'document']
completed_models = []

# print_models(unprinted_designs, completed_models)
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)