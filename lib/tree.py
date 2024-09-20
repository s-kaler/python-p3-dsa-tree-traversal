class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    if self.root is None:
      return None

    if self.root['id'] == id:
        return self.root

    for child in self.root['children']:
        result = Tree(child).get_element_by_id(id)
        if result:
            return result

    return None
