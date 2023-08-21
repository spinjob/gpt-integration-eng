class DataMapper {
  map(source, mapping) {
    const target = {};

    for (const [key, value] of Object.entries(mapping)) {
      const sourceValue = this.getValue(source, value.input.sourcePath);
      this.setValue(target, value.output.path, sourceValue);
    }

    return target;
  }

  getValue(object, path) {
    return path.split('.').reduce((obj, key) => obj[key], object);
  }

  setValue(object, path, value) {
    const keys = path.split('.');
    keys.slice(0, -1).reduce((obj, key) => obj[key] = obj[key] || {}, object)[keys.pop()] = value;
  }
}

module.exports = DataMapper;
