import flake8_import_order
import flake8_import_order.styles


class EventRayStyle(flake8_import_order.styles.Style):
    accepts_application_package_names = True

    @staticmethod
    def name_key(name):
        return name

    @staticmethod
    def sorted_names(names):
        return sorted(names)

    @staticmethod
    def import_key(import_):
        if import_.type == flake8_import_order.ImportType.APPLICATION:
            response = (
                True, import_.package, import_.is_from,
                import_.level, import_.modules, import_.names,
            )
        else:
            response = (
                False, import_.package, import_.is_from, import_.level,
                import_.modules, [],
            )

        return response

    @staticmethod
    def same_section(previous, current) -> bool:
        prev_is_app = previous.type == flake8_import_order.ImportType.APPLICATION
        current_is_app = current.type == flake8_import_order.ImportType.APPLICATION

        result = prev_is_app == current_is_app

        return result

    def check(self):
        yield from super().check()

        for current in self.nodes:
            if not hasattr(current, 'type'):
                continue
            if current.type != flake8_import_order.ImportType.APPLICATION:
                if current.is_from:
                    corrected = 'import %s' % current.modules[0]
                    yield flake8_import_order.styles.Error(
                        current.start_line,
                        'I999',
                        'Only app imports can import names. '
                        'Should be "{0}"'.format(corrected),
                    )
