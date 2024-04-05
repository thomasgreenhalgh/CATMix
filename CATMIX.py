import nuke
import nukescripts
try:
    from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
    from PySide2.QtCore import Qt
    from PySide2.QtGui import QColor
except ImportError:
    try:
        from PySide.QtGui import QApplication, QWidget, QPushButton, QGridLayout
        from PySide.QtCore import Qt
        from PySide.QtGui import QColor
    except ImportError:
        raise ImportError("Neither PySide2 nor PySide is installed. Please install either of them.")

class CATPanel(QWidget):
    def __init__(self, thisnode):
        super(CATPanel, self).__init__()

        self.thisnode = thisnode

        layout = QGridLayout()

        button_info = [
            ("CatA", ["S", "M", "D", "C"]),
            ("CatB", ["S", "M", "D", "C"]),
            ("CatC", ["S", "M", "D", "C"]),
            ("CatD", ["S", "M", "D", "C"]),
            ("CatE", ["S", "M", "D", "C"]),
            ("CatF", ["S", "M", "D", "C"]),
            ("CatG", ["S", "M", "D", "C"]),
            ("CatH", ["S", "M", "D", "C"]),
            ("CatI", ["S", "M", "D", "C"]),
            ("CatJ", ["S", "M", "D", "C"])
        ]

        self.buttons = []
        self.buttons_state = {}

        stored_values = thisnode['StoreVals'].value()
        if stored_values:
            stored_dict = eval(stored_values)
            self.buttons_state.update(stored_dict)

        for row, button_data in enumerate(button_info):
            name, labels = button_data[0], button_data[1]

            name_button = QPushButton(name, enabled=False)
            name_button.setFixedSize(40, 20)
            layout.addWidget(name_button, 0, row, alignment=Qt.AlignHCenter)

            buttons_row = []

            for i, label in enumerate(labels):
                button = QPushButton(label)
                button.setStyleSheet("QPushButton::checked {background-color: red;}")
                button.setCheckable(True)
                button.setFixedSize(40, 20)
                layout.addWidget(button, i + 1, row, alignment=Qt.AlignHCenter)

                if self.buttons_state.get((name, label), False):
                    button.setChecked(True)

                buttons_row.append(button)

                button.clicked.connect(self.create_button_clicked_handler(name, label))

            self.buttons.append(buttons_row)

        self.setLayout(layout)

        self.update_button_colour_for_C()

        self.update_button_colour_for_D()

    def create_button_clicked_handler(self, name, label):
        return lambda: self.execute_action(name, label)

    def execute_action(self, name, label):
        button_state = self.buttons_state.get((name, label), False)

        group_node = self.thisnode


        if name == "CatA":
            if label == "S":
                if button_state:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_CatA')['disable'].setValue(1) 
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
                else:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_CatA')['disable'].setValue(0)
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
            elif label == "M":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Mute_CatA')['disable'].setValue(1)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Mute_CatA')['disable'].setValue(0)
                    group_node.end()
            elif label == "D":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Sat_CatA')['disable'].setValue(0)
                    nuke.toNode('Grad_CatA')['disable'].setValue(0)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Sat_CatA')['disable'].setValue(1)
                    nuke.toNode('Grad_CatA')['disable'].setValue(1)
                    group_node.end()
            elif label == "C":
                if button_state:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_CatA')
                    endDot = nuke.toNode('endDot_CatA')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=False)
                    group_node.end()
                else:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_CatA')
                    endDot = nuke.toNode('endDot_CatA')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=True)
                    group_node.end()

        elif name == "CatB":
            if label == "S":
                if button_state:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_CatB')['disable'].setValue(1) 
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
                else:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_CatB')['disable'].setValue(0)
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
            elif label == "M":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Mute_CatB')['disable'].setValue(1)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Mute_CatB')['disable'].setValue(0)
                    group_node.end()
            elif label == "D":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Sat_CatB')['disable'].setValue(0)
                    nuke.toNode('Grad_CatB')['disable'].setValue(0)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Sat_CatB')['disable'].setValue(1)
                    nuke.toNode('Grad_CatB')['disable'].setValue(1)
                    group_node.end()
            elif label == "C":
                if button_state:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_CatB')
                    endDot = nuke.toNode('endDot_CatB')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=False)
                    group_node.end()
                else:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_CatB')
                    endDot = nuke.toNode('endDot_CatB')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=True)
                    group_node.end()
        if name == "CatC":
            if label == "S":
                if button_state:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_CatC')['disable'].setValue(1) 
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
                else:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_CatC')['disable'].setValue(0)
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
            elif label == "M":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Mute_CatC')['disable'].setValue(1)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Mute_CatC')['disable'].setValue(0)
                    group_node.end()
            elif label == "D":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Sat_CatC')['disable'].setValue(0)
                    nuke.toNode('Grad_CatC')['disable'].setValue(0)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Sat_CatC')['disable'].setValue(1)
                    nuke.toNode('Grad_CatC')['disable'].setValue(1)
                    group_node.end()
            elif label == "C":
                if button_state:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_CatC')
                    endDot = nuke.toNode('endDot_CatC')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=False)
                    group_node.end()
                else:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_CatC')
                    endDot = nuke.toNode('endDot_CatC')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=True)
                    group_node.end()
        elif name == "CatD":
            if label == "S":
                if button_state:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_CatD')['disable'].setValue(1) 
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
                else:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_CatD')['disable'].setValue(0)
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
            elif label == "M":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Mute_CatD')['disable'].setValue(1)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Mute_CatD')['disable'].setValue(0)
                    group_node.end()
            elif label == "D":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Sat_CatD')['disable'].setValue(0)
                    nuke.toNode('Grad_CatD')['disable'].setValue(0)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Sat_CatD')['disable'].setValue(1)
                    nuke.toNode('Grad_CatD')['disable'].setValue(1)
                    group_node.end()
            elif label == "C":
                if button_state:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_CatD')
                    endDot = nuke.toNode('endDot_CatD')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=False)
                    group_node.end()
                else:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_CatD')
                    endDot = nuke.toNode('endDot_CatD')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=True)
                    group_node.end()
        if name == "CatE":
            if label == "S":
                if button_state:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_CatE')['disable'].setValue(1) 
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
                else:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_CatE')['disable'].setValue(0)
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
            elif label == "M":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Mute_CatE')['disable'].setValue(1)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Mute_CatE')['disable'].setValue(0)
                    group_node.end()
            elif label == "D":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Sat_CatE')['disable'].setValue(0)
                    nuke.toNode('Grad_CatE')['disable'].setValue(0)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Sat_CatE')['disable'].setValue(1)
                    nuke.toNode('Grad_CatE')['disable'].setValue(1)
                    group_node.end()
            elif label == "C":
                if button_state:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_CatE')
                    endDot = nuke.toNode('endDot_CatE')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=False)
                    group_node.end()
                else:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_CatE')
                    endDot = nuke.toNode('endDot_CatE')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=True)
                    group_node.end()
        elif name == "CatF":
            if label == "S":
                if button_state:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_CatF')['disable'].setValue(1) 
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
                else:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_CatF')['disable'].setValue(0)
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
            elif label == "M":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Mute_CatF')['disable'].setValue(1)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Mute_CatF')['disable'].setValue(0)
                    group_node.end()
            elif label == "D":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Sat_CatF')['disable'].setValue(0)
                    nuke.toNode('Grad_CatF')['disable'].setValue(0)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Sat_CatF')['disable'].setValue(1)
                    nuke.toNode('Grad_CatF')['disable'].setValue(1)
                    group_node.end()
            elif label == "C":
                if button_state:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_CatF')
                    endDot = nuke.toNode('endDot_CatF')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=False)
                    group_node.end()
                else:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_CatF')
                    endDot = nuke.toNode('endDot_CatF')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=True)
                    group_node.end()
        if name == "CatG":
            if label == "S":
                if button_state:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_CatG')['disable'].setValue(1) 
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
                else:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_CatG')['disable'].setValue(0)
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
            elif label == "M":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Mute_CatG')['disable'].setValue(1)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Mute_CatG')['disable'].setValue(0)
                    group_node.end()
            elif label == "D":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Sat_CatG')['disable'].setValue(0)
                    nuke.toNode('Grad_CatG')['disable'].setValue(0)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Sat_CatG')['disable'].setValue(1)
                    nuke.toNode('Grad_CatG')['disable'].setValue(1)
                    group_node.end()
            elif label == "C":
                if button_state:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_CatG')
                    endDot = nuke.toNode('endDot_CatG')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=False)
                    group_node.end()
                else:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_CatG')
                    endDot = nuke.toNode('endDot_CatG')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=True)
                    group_node.end()
        elif name == "CatH":
            if label == "S":
                if button_state:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_CatH')['disable'].setValue(1) 
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
                else:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_CatH')['disable'].setValue(0)
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
            elif label == "M":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Mute_CatH')['disable'].setValue(1)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Mute_CatH')['disable'].setValue(0)
                    group_node.end()
            elif label == "D":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Sat_CatH')['disable'].setValue(0)
                    nuke.toNode('Grad_CatH')['disable'].setValue(0)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Sat_CatH')['disable'].setValue(1)
                    nuke.toNode('Grad_CatH')['disable'].setValue(1)
                    group_node.end()
            elif label == "C":
                if button_state:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_CatH')
                    endDot = nuke.toNode('endDot_CatH')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=False)
                    group_node.end()
                else:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_CatH')
                    endDot = nuke.toNode('endDot_CatH')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=True)
                    group_node.end()
        if name == "CatI":
            if label == "S":
                if button_state:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_CatI')['disable'].setValue(1) 
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
                else:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_CatI')['disable'].setValue(0)
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
            elif label == "M":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Mute_CatI')['disable'].setValue(1)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Mute_CatI')['disable'].setValue(0)
                    group_node.end()
            elif label == "D":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Sat_CatI')['disable'].setValue(0)
                    nuke.toNode('Grad_CatI')['disable'].setValue(0)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Sat_CatI')['disable'].setValue(1)
                    nuke.toNode('Grad_CatI')['disable'].setValue(1)
                    group_node.end()
            elif label == "C":
                if button_state:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_CatI')
                    endDot = nuke.toNode('endDot_CatI')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=False)
                    group_node.end()
                else:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_CatI')
                    endDot = nuke.toNode('endDot_CatI')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=True)
                    group_node.end()
        elif name == "CatJ":
            if label == "S":
                if button_state:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_CatJ')['disable'].setValue(1) 
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
                else:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_CatJ')['disable'].setValue(0)
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
            elif label == "M":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Mute_CatJ')['disable'].setValue(1)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Mute_CatJ')['disable'].setValue(0)
                    group_node.end()
            elif label == "D":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Sat_CatJ')['disable'].setValue(0)
                    nuke.toNode('Grad_CatJ')['disable'].setValue(0)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Sat_CatJ')['disable'].setValue(1)
                    nuke.toNode('Grad_CatJ')['disable'].setValue(1)
                    group_node.end()
            elif label == "C":
                if button_state:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_CatJ')
                    endDot = nuke.toNode('endDot_CatJ')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=False)
                    group_node.end()
                else:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_CatJ')
                    endDot = nuke.toNode('endDot_CatJ')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=True)
                    group_node.end()

        self.buttons_state[(name, label)] = not button_state
        self.thisnode['StoreVals'].setValue(str(self.buttons_state))
    @staticmethod
    def solo_passes(group_node):
        group_node.begin()
        solo_node = nuke.toNode('SOLOPASSES')
        solo_node.begin()
        cat_list = ['Merge_CatA', 'Merge_CatB', 'Merge_CatC', 'Merge_CatD', 'Merge_CatE', 'Merge_CatF', 'Merge_CatG', 'Merge_CatH', 'Merge_CatI', 'Merge_CatJ']
        aov_list = ['Merge_Albedo', 'Merge_Coat', 'Merge_Diffuse', 'Merge_Emission', 'Merge_EmissionInd', 'Merge_Sheen', 'Merge_Specular', 'Merge_SSS', 'Merge_Transmission', 'Merge_Leftovers']
        
        light_switch_value = 0
        
        for node_name in cat_list:
            if not nuke.toNode(node_name)['disable'].getValue():
                light_switch_value = 1
                break
        
        if light_switch_value != 1:
            for node_name in aov_list:
                if not nuke.toNode(node_name)['disable'].getValue():
                    light_switch_value = 2
                    break
        
        nuke.toNode('LightSwitch')['which'].setValue(light_switch_value)
        
        solo_node.end()
        group_node.end()

    def disable_nodes_between(self, start_dot, end_dot, disable=True):
        visited_nodes = set()

        def disable_nodes_recursive(node):
            if node in visited_nodes or node == start_dot:
                return
            visited_nodes.add(node)

            for input_node in node.dependencies(nuke.INPUTS | nuke.HIDDEN_INPUTS):
                disable_nodes_recursive(input_node)

            disable_knob = node.knob('disable')
            if disable_knob is not None:
                disable_knob.setValue(disable)

        disable_nodes_recursive(end_dot)

    def update_button_colour_for_C(self):
        group_node = self.thisnode

        for row_index, button_row in enumerate(self.buttons):
            start_dot = nuke.toNode('startDot_Cat' + chr(ord('A') + row_index))
            end_dot = nuke.toNode('endDot_Cat' + chr(ord('A') + row_index))

            button_C = button_row[3]
            if button_C:
                if end_dot not in start_dot.dependent():
                    colour = 'blue'
                    button_C.setStyleSheet('QPushButton {background-color: %s;}' % colour)
            else:
                None


    def update_button_colour_for_D(self):
        group_node = self.thisnode

        for row_index, button_row in enumerate(self.buttons):
            group_node.begin()
            saturation_knob_name = 'Sat_Cat' + chr(ord('A') + row_index)
            saturation_knob = nuke.toNode(saturation_knob_name)['saturation']
            grade_knob_name = 'Grad_Cat' + chr(ord('A') + row_index)
            white_knob = nuke.toNode(grade_knob_name)['white']
            multiply_knob = nuke.toNode(grade_knob_name)['multiply']
            add_knob = nuke.toNode(grade_knob_name)['add']
            gamma_knob = nuke.toNode(grade_knob_name)['gamma']
            group_node.end()

            saturation_default_value = 1.0
            white_default_value = 1.0
            multiply_default_value = 1.0
            add_default_value = 0.0
            gamma_default_value = 1.0

            button_D = button_row[2]
            if button_D:  
                if (saturation_knob and saturation_knob.value() != saturation_default_value) or \
                        (white_knob and white_knob.value() != white_default_value) or \
                        (multiply_knob and multiply_knob.value() != multiply_default_value) or \
                        (add_knob and add_knob.value() != add_default_value) or \
                        (gamma_knob and gamma_knob.value() != gamma_default_value):
                    colour = 'green'
                else:
                    colour = None

                button_D.setStyleSheet('QPushButton {background-color: %s;}' % colour)



    def makeUI(self):
        return self


class AOVPanel(QWidget):
    def __init__(self, thisnode):
        super(AOVPanel, self).__init__()

        self.thisnode = thisnode

        layout = QGridLayout()

        button_info = [
            ("Albedo", ["S", "M", "D", "C"]),
            ("Coat", ["S", "M", "D", "C"]),
            ("Diffuse", ["S", "M", "D", "C"]),
            ("Emission", ["S", "M", "D", "C"]),
            ("EmissionInd", ["S", "M", "D", "C"]),
            ("Sheen", ["S", "M", "D", "C"]),
            ("Specular", ["S", "M", "D", "C"]),
            ("SSS", ["S", "M", "D", "C"]),
            ("Transmission", ["S", "M", "D", "C"]),
            ("Leftovers", ["S", "M", "D", "C"])
        ]

        self.buttons = []
        self.buttons_state = {}

        stored_values = thisnode['StoreVals'].value()
        if stored_values:
            stored_dict = eval(stored_values)
            self.buttons_state.update(stored_dict)

        for row, button_data in enumerate(button_info):
            name, labels = button_data[0], button_data[1]

            name_button = QPushButton(name, enabled=False)
            name_button.setFixedSize(40, 20)
            layout.addWidget(name_button, 0, row, alignment=Qt.AlignHCenter)

            buttons_row = []

            for i, label in enumerate(labels):
                button = QPushButton(label)
                button.setStyleSheet("QPushButton::checked {background-color: red;}")
                button.setCheckable(True)
                button.setFixedSize(40, 20)
                layout.addWidget(button, i + 1, row, alignment=Qt.AlignHCenter)

                if self.buttons_state.get((name, label), False):
                    button.setChecked(True)

                buttons_row.append(button)

                button.clicked.connect(self.create_button_clicked_handler(name, label))

            self.buttons.append(buttons_row)

        self.setLayout(layout)

        self.update_button_colour_for_C()

        self.update_button_colour_for_D()

    def create_button_clicked_handler(self, name, label):
        return lambda: self.execute_action(name, label)

    def execute_action(self, name, label):
        button_state = self.buttons_state.get((name, label), False)

        group_node = self.thisnode


        if name == "Albedo":
            if label == "S":
                if button_state:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_Albedo')['disable'].setValue(1) 
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
                else:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_Albedo')['disable'].setValue(0)
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
            elif label == "M":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Mute_Albedo')['disable'].setValue(1)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Mute_Albedo')['disable'].setValue(0)
                    group_node.end()
            elif label == "D":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Sat_Albedo')['disable'].setValue(0)
                    nuke.toNode('Grad_Albedo')['disable'].setValue(0)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Sat_Albedo')['disable'].setValue(1)
                    nuke.toNode('Grad_Albedo')['disable'].setValue(1)
                    group_node.end()
            elif label == "C":
                if button_state:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_Albedo')
                    endDot = nuke.toNode('endDot_Albedo')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=False)
                    group_node.end()
                else:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_Albedo')
                    endDot = nuke.toNode('endDot_Albedo')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=True)
                    group_node.end()

        elif name == "Coat":
            if label == "S":
                if button_state:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_Coat')['disable'].setValue(1) 
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
                else:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_Coat')['disable'].setValue(0)
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
            elif label == "M":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Mute_Coat')['disable'].setValue(1)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Mute_Coat')['disable'].setValue(0)
                    group_node.end()
            elif label == "D":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Sat_Coat')['disable'].setValue(0)
                    nuke.toNode('Grad_Coat')['disable'].setValue(0)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Sat_Coat')['disable'].setValue(1)
                    nuke.toNode('Grad_Coat')['disable'].setValue(1)
                    group_node.end()
            elif label == "C":
                if button_state:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_Coat')
                    endDot = nuke.toNode('endDot_Coat')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=False)
                    group_node.end()
                else:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_Coat')
                    endDot = nuke.toNode('endDot_Coat')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=True)
                    group_node.end()
        if name == "Diffuse":
            if label == "S":
                if button_state:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_Diffuse')['disable'].setValue(1) 
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
                else:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_Diffuse')['disable'].setValue(0)
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
            elif label == "M":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Mute_Diffuse')['disable'].setValue(1)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Mute_Diffuse')['disable'].setValue(0)
                    group_node.end()
            elif label == "D":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Sat_Diffuse')['disable'].setValue(0)
                    nuke.toNode('Grad_Diffuse')['disable'].setValue(0)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Sat_Diffuse')['disable'].setValue(1)
                    nuke.toNode('Grad_Diffuse')['disable'].setValue(1)
                    group_node.end()
            elif label == "C":
                if button_state:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_Diffuse')
                    endDot = nuke.toNode('endDot_Diffuse')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=False)
                    group_node.end()
                else:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_Diffuse')
                    endDot = nuke.toNode('endDot_Diffuse')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=True)
                    group_node.end()
        elif name == "Emission":
            if label == "S":
                if button_state:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_Emission')['disable'].setValue(1) 
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
                else:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_Emission')['disable'].setValue(0)
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
            elif label == "M":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Mute_Emission')['disable'].setValue(1)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Mute_Emission')['disable'].setValue(0)
                    group_node.end()
            elif label == "D":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Sat_Emission')['disable'].setValue(0)
                    nuke.toNode('Grad_Emission')['disable'].setValue(0)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Sat_Emission')['disable'].setValue(1)
                    nuke.toNode('Grad_Emission')['disable'].setValue(1)
                    group_node.end()
            elif label == "C":
                if button_state:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_Emission')
                    endDot = nuke.toNode('endDot_Emission')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=False)
                    group_node.end()
                else:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_Emission')
                    endDot = nuke.toNode('endDot_Emission')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=True)
                    group_node.end()
        if name == "EmissionInd":
            if label == "S":
                if button_state:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_EmissionInd')['disable'].setValue(1) 
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
                else:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_EmissionInd')['disable'].setValue(0)
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
            elif label == "M":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Mute_EmissionInd')['disable'].setValue(1)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Mute_EmissionInd')['disable'].setValue(0)
                    group_node.end()
            elif label == "D":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Sat_EmissionInd')['disable'].setValue(0)
                    nuke.toNode('Grad_EmissionInd')['disable'].setValue(0)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Sat_EmissionInd')['disable'].setValue(1)
                    nuke.toNode('Grad_EmissionInd')['disable'].setValue(1)
                    group_node.end()
            elif label == "C":
                if button_state:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_EmissionInd')
                    endDot = nuke.toNode('endDot_EmissionInd')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=False)
                    group_node.end()
                else:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_EmissionInd')
                    endDot = nuke.toNode('endDot_EmissionInd')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=True)
                    group_node.end()
        elif name == "Sheen":
            if label == "S":
                if button_state:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_Sheen')['disable'].setValue(1) 
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
                else:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_Sheen')['disable'].setValue(0)
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
            elif label == "M":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Mute_Sheen')['disable'].setValue(1)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Mute_Sheen')['disable'].setValue(0)
                    group_node.end()
            elif label == "D":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Sat_Sheen')['disable'].setValue(0)
                    nuke.toNode('Grad_Sheen')['disable'].setValue(0)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Sat_Sheen')['disable'].setValue(1)
                    nuke.toNode('Grad_Sheen')['disable'].setValue(1)
                    group_node.end()
            elif label == "C":
                if button_state:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_Sheen')
                    endDot = nuke.toNode('endDot_Sheen')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=False)
                    group_node.end()
                else:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_Sheen')
                    endDot = nuke.toNode('endDot_Sheen')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=True)
                    group_node.end()
        if name == "Specular":
            if label == "S":
                if button_state:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_Specular')['disable'].setValue(1) 
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
                else:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_Specular')['disable'].setValue(0)
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
            elif label == "M":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Mute_Specular')['disable'].setValue(1)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Mute_Specular')['disable'].setValue(0)
                    group_node.end()
            elif label == "D":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Sat_Specular')['disable'].setValue(0)
                    nuke.toNode('Grad_Specular')['disable'].setValue(0)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Sat_Specular')['disable'].setValue(1)
                    nuke.toNode('Grad_Specular')['disable'].setValue(1)
                    group_node.end()
            elif label == "C":
                if button_state:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_Specular')
                    endDot = nuke.toNode('endDot_Specular')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=False)
                    group_node.end()
                else:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_Specular')
                    endDot = nuke.toNode('endDot_Specular')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=True)
                    group_node.end()
        elif name == "SSS":
            if label == "S":
                if button_state:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_SSS')['disable'].setValue(1) 
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
                else:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_SSS')['disable'].setValue(0)
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
            elif label == "M":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Mute_SSS')['disable'].setValue(1)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Mute_SSS')['disable'].setValue(0)
                    group_node.end()
            elif label == "D":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Sat_SSS')['disable'].setValue(0)
                    nuke.toNode('Grad_SSS')['disable'].setValue(0)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Sat_SSS')['disable'].setValue(1)
                    nuke.toNode('Grad_SSS')['disable'].setValue(1)
                    group_node.end()
            elif label == "C":
                if button_state:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_SSS')
                    endDot = nuke.toNode('endDot_SSS')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=False)
                    group_node.end()
                else:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_SSS')
                    endDot = nuke.toNode('endDot_SSS')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=True)
                    group_node.end()
        if name == "Transmission":
            if label == "S":
                if button_state:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_Transmission')['disable'].setValue(1) 
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
                else:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_Transmission')['disable'].setValue(0)
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
            elif label == "M":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Mute_Transmission')['disable'].setValue(1)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Mute_Transmission')['disable'].setValue(0)
                    group_node.end()
            elif label == "D":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Sat_Transmission')['disable'].setValue(0)
                    nuke.toNode('Grad_Transmission')['disable'].setValue(0)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Sat_Transmission')['disable'].setValue(1)
                    nuke.toNode('Grad_Transmission')['disable'].setValue(1)
                    group_node.end()
            elif label == "C":
                if button_state:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_Transmission')
                    endDot = nuke.toNode('endDot_Transmission')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=False)
                    group_node.end()
                else:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_Transmission')
                    endDot = nuke.toNode('endDot_Transmission')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=True)
                    group_node.end()
        elif name == "Leftovers":
            if label == "S":
                if button_state:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_Leftovers')['disable'].setValue(1) 
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
                else:
                    group_node.begin()
                    solo_node = nuke.toNode('SOLOPASSES')
                    solo_node.begin()
                    nuke.toNode('Merge_Leftovers')['disable'].setValue(0)
                    solo_node.end()
                    group_node.end()
                    self.solo_passes(group_node)
            elif label == "M":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Mute_Leftovers')['disable'].setValue(1)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Mute_Leftovers')['disable'].setValue(0)
                    group_node.end()
            elif label == "D":
                if button_state:
                    group_node.begin()
                    nuke.toNode('Sat_Leftovers')['disable'].setValue(0)
                    nuke.toNode('Grad_Leftovers')['disable'].setValue(0)
                    group_node.end()
                else:
                    group_node.begin()
                    nuke.toNode('Sat_Leftovers')['disable'].setValue(1)
                    nuke.toNode('Grad_Leftovers')['disable'].setValue(1)
                    group_node.end()
            elif label == "C":
                if button_state:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_Leftovers')
                    endDot = nuke.toNode('endDot_Leftovers')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=False)
                    group_node.end()
                else:
                    group_node.begin()
                    startDot = nuke.toNode('startDot_Leftovers')
                    endDot = nuke.toNode('endDot_Leftovers')

                    if startDot and endDot:
                        self.disable_nodes_between(startDot, endDot, disable=True)
                    group_node.end()

        self.buttons_state[(name, label)] = not button_state
        self.thisnode['StoreVals'].setValue(str(self.buttons_state))

    @staticmethod
    def solo_passes(group_node):
        group_node.begin()
        solo_node = nuke.toNode('SOLOPASSES')
        solo_node.begin()
        cat_list = ['Merge_CatA', 'Merge_CatB', 'Merge_CatC', 'Merge_CatD', 'Merge_CatE', 'Merge_CatF', 'Merge_CatG', 'Merge_CatH', 'Merge_CatI', 'Merge_CatJ']
        aov_list = ['Merge_Albedo', 'Merge_Coat', 'Merge_Diffuse', 'Merge_Emission', 'Merge_EmissionInd', 'Merge_Sheen', 'Merge_Specular', 'Merge_SSS', 'Merge_Transmission', 'Merge_Leftovers']
        
        light_switch_value = 0
        
        for node_name in cat_list:
            if not nuke.toNode(node_name)['disable'].getValue():
                light_switch_value = 1
                break
        
        if light_switch_value != 1:
            for node_name in aov_list:
                if not nuke.toNode(node_name)['disable'].getValue():
                    light_switch_value = 2
                    break
        
        nuke.toNode('LightSwitch')['which'].setValue(light_switch_value)
        
        solo_node.end()
        group_node.end()

    def disable_nodes_between(self, start_dot, end_dot, disable=True):
        visited_nodes = set()

        def disable_nodes_recursive(node):
            if node in visited_nodes or node == start_dot:
                return
            visited_nodes.add(node)

            for input_node in node.dependencies(nuke.INPUTS | nuke.HIDDEN_INPUTS):
                disable_nodes_recursive(input_node)

            disable_knob = node.knob('disable')
            if disable_knob is not None:
                disable_knob.setValue(disable)

        disable_nodes_recursive(end_dot)

    def update_button_colour_for_C(self):
        group_node = self.thisnode
        categories = ['Albedo', 'Coat', 'Diffuse', 'Emission', 'EmissionInd', 'Sheen', 'Specular', 'SSS', 'Transmission', 'Leftovers']

        for row_index, button_row in enumerate(self.buttons):
            start_dot = nuke.toNode('startDot_' + categories[row_index])
            end_dot = nuke.toNode('endDot_' + categories[row_index])

            button_C = button_row[3]
            if button_C:
                if end_dot not in start_dot.dependent():
                    colour = 'blue'
                    button_C.setStyleSheet('QPushButton {background-color: %s;}' % colour)
            else:
                None

    def update_button_colour_for_D(self):
        group_node = self.thisnode

        categories = ['Albedo', 'Coat', 'Diffuse', 'Emission', 'EmissionInd', 'Sheen', 'Specular', 'SSS', 'Transmission', 'Leftovers']

        for row_index, button_row in enumerate(self.buttons):
            group_node.begin()
            saturation_knob_name = 'Sat_' + categories[row_index]
            saturation_knob = nuke.toNode(saturation_knob_name)['saturation']
            grade_knob_name = 'Grad_' + categories[row_index]
            white_knob = nuke.toNode(grade_knob_name)['white']
            multiply_knob = nuke.toNode(grade_knob_name)['multiply']
            add_knob = nuke.toNode(grade_knob_name)['add']
            gamma_knob = nuke.toNode(grade_knob_name)['gamma']
            group_node.end()
            
            saturation_default_value = 1.0
            white_default_value = 1.0
            multiply_default_value = 1.0
            add_default_value = 0.0
            gamma_default_value = 1.0
            
            button_D = button_row[2]
            if button_D:
                if (saturation_knob and saturation_knob.value() != saturation_default_value) or \
                    (white_knob and white_knob.value() != white_default_value) or \
                    (multiply_knob and multiply_knob.value() != multiply_default_value) or \
                    (add_knob and add_knob.value() != add_default_value) or \
                    (gamma_knob and gamma_knob.value() != gamma_default_value):
                    colour = 'green'
                else:
                    colour = None
                
                button_D.setStyleSheet('QPushButton {background-color: %s;}' % colour)



    def makeUI(self):
        return self
