import model_read
import model_write
import view

def button_click():
    type = view.get_type_of_operation()
    
    if type == 'w':
        model_write.write_file('phone_book.txt', input('Запишите контакт в следующем порядке: id, имя, фамилию, номер телефона, комментрий. через запятую как в инструкции.'))
    elif type == 'r':
        model_read.read_file('phone_book.txt')