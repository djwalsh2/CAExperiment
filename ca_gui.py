"""
Description:
    Prototype GUI for Generating Cellular Automata Jobs
Author:
    David Walsh (2019)
"""
import tkinter as tk
from tkinter import messagebox

JOBS_DIRECTORY = "jobs/"

"""
CA GUI Class
"""


class CaGui(tk.Frame):

    def __init__(self, master):
        self.master = master
        super().__init__()

        # window title
        self.tile = 'CA Generator'
        master.title(self.tile)

        # prevent resizing
        self.master.resizable(False, False)

        # window size
        self.window_size = '250x150'
        master.geometry(self.window_size)

        # menu
        self.menu = tk.Menu(master)
        file_menu = tk.Menu(self.menu)
        master.config(menu=self.menu)
        self.menu.add_cascade(labe='File', menu=file_menu)
        file_menu.add_command(label='Exit', command=self.on_exit)

        self.help_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label='Help', menu=self.help_menu)
        self.help_menu.add_command(label='About')

        # rule number
        self.rule_number_entry_label = tk.Label(master, anchor="w",
                                                text='Rule Number:').grid(row=0)
        self.rule_number_entry = tk.Entry(master)
        self.rule_number_entry.grid(row=0, column=1)

        # rule radius
        self.rule_radius_entry_label = tk.Label(master, anchor="w",
                                                text='Rule Radius:').grid(row=1)
        self.rule_radius_entry = tk.Entry(master)
        self.rule_radius_entry.grid(row=1, column=1)

        # rule configuration
        self.rule_configuration_entry_label = tk.Label(master, anchor="w",
                                                       text='Rule Configuration:').grid(row=2)
        self.rule_configuration_entry = tk.Entry(master)
        self.rule_configuration_entry.grid(row=2, column=1)

        # rule length
        self.rule_length_entry_label = tk.Label(master, anchor="w",
                                                text='Rule Length:').grid(row=3)
        self.rule_length_entry = tk.Entry(master)
        self.rule_length_entry.grid(row=3, column=1)

        # rule generation
        self.rule_generation_entry_label = tk.Label(master, anchor="w",
                                                    text='Rule Generation:').grid(row=4)
        self.rule_generation_entry = tk.Entry(master)
        self.rule_generation_entry.grid(row=4, column=1)

        # submit button
        self.submit_button = tk.Button(master, text='Submit Job',
                                    command=self.submit_job).grid(row=5,
                                                                  columnspan=2)

    def submit_job(self):
        entry_string = self.get_job_string()

        if len(entry_string) < 4:
            tk.messagebox.showerror("Error", "Please ensure all fields are "
                                             "filled out.")
        else:
            self.validate_fields(entry_string)
            file = JOBS_DIRECTORY + entry_string[0] + "_" + entry_string[1] + \
                "_" + entry_string[2] + "_" + entry_string[3] + "_" + \
                entry_string[4] + ".txt"
            self.write_job_file(file, entry_string)
            print('Success...Job Submitted!')

    @staticmethod
    def validate_fields(fields):

        rule_number = fields[0]
        rule_radius = fields[1]
        rule_configuration = fields[2]
        rule_length = fields[3]
        rule_generation = fields[4]

        """
        Validate rule number
        """
        try:
            rn = int(rule_number)
        except ValueError:
            tk.messagebox.showerror("Error", "Rule number must be a"
                                             " non-negative integer.")

        """
        Validate rule radius
        """
        try:
            rr = int(rule_radius)
        except ValueError:
            tk.messagebox.showerror("Error", "Rule radius must be a"
                                             " non-negative integer.")

        """
        Validate rule configuration
        """
        try:
            rc = int(rule_configuration)
        except ValueError:
            tk.messagebox.showerror("Error", "Rule radius must be a"
                                             " non-negative integer.")

        """
        Validate rule length
        """
        try:
            rl = int(rule_length)
        except ValueError:
            tk.messagebox.showerror("Error", "Rule radius must be a"
                                             " non-negative integer.")

        """
        Validate rule generation
        """
        try:
            rg = int(rule_generation)
        except ValueError:
            tk.messagebox.showerror("Error", "Rule generation must be a "
                                             " non-negative integer.")

    def get_job_string(self):
        rule_number = self.rule_number_entry.get()
        rule_radius = self.rule_radius_entry.get()
        rule_configuration = self.rule_configuration_entry.get()
        rule_configuration_length = self.rule_length_entry.get()
        rule_generation_length = self.rule_generation_entry.get()

        s = str(rule_number) + " " +\
            str(rule_radius) + " " + \
            str(rule_configuration) + " " + \
            str(rule_configuration_length) + " " + \
            str(rule_generation_length)

        s = s.split()
        return s

    @staticmethod
    def write_job_file(path, string):
        file = open(path, "w+")
        string = ' '.join(string)
        file.write(str(string))
        file.close()

    def on_exit(self):
        self.quit()


"""
Main
"""


def main():
    root = tk.Tk()
    ca_gui = CaGui(root)
    root.mainloop()


if __name__ == '__main__':
    main()
