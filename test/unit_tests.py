import unittest
from unittest.mock import patch
import app
import sys


class Test_class(unittest.TestCase):

    def setUp(self):
        with patch('app.input', return_value='q'):
            app.secretary_program_start()

    def test_def_list(self):
        '''тест команды, которая выведет список всех документов '''

        orig_stdout = sys.stdout
        test_file = open('test.txt', 'w', encoding='utf-8')
        sys.stdout = test_file
        app.show_all_docs_info()
        sys.stdout = orig_stdout
        test_file.close()

        with open('test.txt', encoding='utf-8') as file:
            data = file.read()
        self.assertEqual('Список всех документов:\n'
                      '\npassport "2207 876234" "Василий Гупкин"\n'
                      'invoice "11-2" "Геннадий Покемонов"\n'
                      'insurance "10006" "Аристарх Павлов"\n', data)

    def test_get_doc_shelf(self):
        '''тест функции команды, которая спросит номер документа и
         выведет номер полки, на которой он находится'''
        with patch('app.input', return_value='11-2'):
            app.get_doc_shelf()
            self.assertEqual('1', app.get_doc_shelf())

    def test_get_doc_owner_name(self):
        """тест команды, которая спросит номер документа и
        выведет имя человека, которому он принадлежит"""
        with patch ('app.input', return_value='11-2'):
            app.get_doc_owner_name()
            self.assertEqual('Геннадий Покемонов', app.get_doc_owner_name())

    def test_get_all_doc_owners_names(self):
        """тест команды, которая выводит список всех владельцев документов"""
        data = {'Геннадий Покемонов', 'Аристарх Павлов', 'Василий Гупкин'}
        self.assertEqual(data, app.get_all_doc_owners_names())


    def test_add_new_doc(self):
        '''тест команды, которая добавит новый
        документ в каталог и в перечень полок'''
        with patch('app.input', side_effect=[12121, 'passport', 'Vladislav', 2]):
            app.add_new_doc()
            self.assertIn({'type': 'passport', 'number': 12121, 'name': 'Vladislav'}, app.documents)

    def test_delete_doc(self):
        """тест команды, которая спросит номер документа и
         удалит его из каталога и из перечня полок"""
        data = {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"}
        with patch('app.input', return_value='11-2'):
            app.delete_doc()
            self.assertNotIn(data, app.documents)

    def test_move_doc_to_shelf(self):
        """тест команды, которая спросит номер документа и
        целевую полку и переместит его с текущей полки на целевую"""
        self.assertNotIn('11-2', app.directories['2'])
        with patch('app.input', side_effect=['11-2','2']):
            app.move_doc_to_shelf()
            self.assertIn('11-2', app.directories['2'])

    def test_add_new_shelf(self):
        """тест команды, которая спросит номер новой полки и
         добавит ее в перечень"""
        self.assertNotIn('5', app.directories.keys())
        with patch('app.input', return_value='5'):
            app.add_new_shelf()
            self.assertIn('5', app.directories.keys())



