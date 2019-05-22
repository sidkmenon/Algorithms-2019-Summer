PROGRAMS = median
all: $(PROGRAMS)

ALLPROGRAMS = $(PROGRAMS)

include ./common/rules.mk

%.o: %.cc $(BUILDSTAMP)
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) $(DEPCFLAGS) $(O) -o $@ -c $<

median: median.o
	$(CXX) $(CXXFLAGS) $(O) -o $@ $^

clean:
	rm -rf $(ALLPROGRAMS) runevil *.o $(DEPSDIR)

.PHONY: all clean
