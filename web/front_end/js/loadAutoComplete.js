import Autocomplete from './autocomplete.js';

function loadAutoCompleteInput() {
    Autocomplete.init("input.autocomplete", {
                items: [
                    {
                        id: 'opt1',
                        label: 'Option 1',
                        value: 'opt1',
                        title: 'Option 1',
                        data: {
                            key: 1
                        },
                    },
    {
      id: 'opt2',
      label: 'Option 2',
      value: 'opt1',
      title: 'Option 2',
      data: {
        key: 2
      },
    }
  ],
  valueField: "id",
  labelField: "title",
});
}

export default loadAutoCompleteInput;
